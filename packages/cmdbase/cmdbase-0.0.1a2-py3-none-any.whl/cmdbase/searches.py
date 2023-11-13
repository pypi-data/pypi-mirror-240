from __future__ import annotations
import logging
import re
from psycopg.sql import SQL, Identifier
from zut import slugify
from .utils import get_jsonb_sql
from .models import Category, CategoryProp, Item
from .commons import execute_as_dicts


logger = logging.getLogger(__name__)

def search(search: str, limit: int = 20) -> list:
    if not search:
        return []
    
    search_prop = None
    pos = search.find(':')
    if pos > 0:
        if key := search[0:pos].strip():
            if val := search[pos+1:].strip():
                search_prop = key
                search = val
    
    if (search.startswith('"') and search.endswith('"')) or (search.startswith("'") and search.endswith("'")):
        search_exact = True
        search = search[1:-1]
    elif re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", search): # UUID
        search_exact = True
    else:
        search_exact = False
        search = slugify(search, keep='%')
        search_suffix = search + ('%' if not search.endswith('%') else '')
        search_full = ('%' if not search_suffix.startswith('%') else '') + search_suffix

    logger.debug("search: %s, exact: %s", search, search_exact)

    limit = int(limit)        
    item_ids = set()
    all_results = []   

    # Search categories
    if not search_prop:
        params = []
        sql =    "SELECT null AS category_name, null AS category_slug, name AS name, slug AS slug, 'category' AS source, null AS value"
        sql += "\nFROM {}"; params += [Identifier(Category._meta.db_table)]
        if search_exact:
            sql += "\nWHERE name = {}"; params += [search]
        else:
            sql += "\nWHERE slug LIKE {}"; params += [search_full]
        sql += "\nLIMIT %d" % (limit,)

        results = execute_as_dicts(SQL(sql).format(*params))
        for result in results:
            all_results.append(result)
            
        if len(all_results) >= limit:
            return all_results

    # Search items by name (using suffix-wildcard if not exact)
    if not search_prop or search_prop == 'name':
        params = []
        sql =    "SELECT i.id, c.name AS category_name, c.slug AS category_slug, i.name, i.slug, 'name' AS source, null AS value"
        sql += "\nFROM {} i INNER JOIN {} c ON c.id = i.category_id"; params += [Identifier(Item._meta.db_table), Identifier(Category._meta.db_table)]
        if search_exact:
            sql += "\nWHERE i.name = {}"; params += [search]
        else:
            sql += "\nWHERE i.slug LIKE {}"; params += [search_suffix]
        sql += "\nLIMIT %d" % (limit - len(all_results),)

        results = execute_as_dicts(SQL(sql).format(*params))
        for result in results:
            item_ids.add(result.pop('id'))
            all_results.append(result)
            
        if len(all_results) >= limit:
            return all_results

    # Search items by name using prefix-wildcard 
    # NOTE: do prefix-wildcard matching on items the latest possible (so that index can be used)
    if not search_exact and (not search_prop or search_prop == 'name'):
        params = []
        sql =    "SELECT i.id, c.name AS category_name, c.slug AS category_slug, i.name, i.slug, 'name (wildcard)' AS source, null AS value"
        sql += "\nFROM {} i INNER JOIN {} c ON c.id = i.category_id"; params += [Identifier(Item._meta.db_table), Identifier(Category._meta.db_table)]
        sql += "\nWHERE i.slug LIKE {}"; params += [search_full]
        if item_ids:
            sql += "\nAND i.id NOT IN (%s)" % (','.join(str(id) for id in item_ids),)
        sql += "\nLIMIT %d" % (limit - len(all_results),)

        results = execute_as_dicts(SQL(sql).format(*params))
        for result in results:
            item_ids.add(result.pop('id'))
            all_results.append(result)
            
        if len(all_results) >= limit:
            return all_results

    # Search data fields
    if search_prop:
        if search_prop != 'name':
            params = []
            sql =    "SELECT category_name, category_slug, name, slug, source, value"
            sql += "\nFROM ("
            sql += "\n    SELECT c.name AS category_name, c.slug AS category_slug, i.name, i.slug, {} AS source, {} AS value"; params += [search_prop, get_jsonb_sql('i.data', search_prop, as_text=True)]
            sql += "\n    FROM {} i"; params += [Identifier(Item._meta.db_table)]
            sql += "\n    INNER JOIN {} c ON c.id = i.category_id"; params += [Identifier(Category._meta.db_table)]
            if item_ids:
                sql += "\n    WHERE i.id NOT IN (%s)" % (','.join(str(id) for id in item_ids),)
            sql += "\n) s"
            if search_exact:
                sql += "\nWHERE value = {}"; params += [search]
            else:
                sql += "\nWHERE slugify(value) LIKE {}"; params += [search_full]
            sql += "\nLIMIT %d" % (limit - len(all_results),)
            
            results = execute_as_dicts(SQL(sql).format(*params))
            for result in results:
                all_results.append(result)

    else:
        params = []
        sql =    "SELECT category_name, category_slug, name, slug, source, value"
        sql += "\nFROM ("
        sql += "\n    SELECT s.*, ROW_NUMBER() OVER (PARTITION BY s.id ORDER BY s.source_ordinal) AS rown"
        sql += "\n    FROM ("
        sql += "\n        SELECT i.id, c.category_name, c.category_slug, i.name, i.slug, c.prop_name AS source, c.prop_ordinal AS source_ordinal, jsonb_extract_path_text(i.data, c.prop_name) AS value"
        sql += "\n        FROM {} i"; params += [Identifier(Item._meta.db_table)]
        sql += "\n        INNER JOIN {} c ON c.category_id = i.category_id"; params += [Identifier(CategoryProp._meta.db_table)]
        sql += "\n        WHERE c.prop_search"

        if item_ids:
            sql += "\n        AND i.id NOT IN (%s)" % (','.join(str(id) for id in item_ids),)

        sql += "\n    ) s"

        if search_exact:
            sql += "\n    WHERE value = {}"; params += [search]
        else:
            sql += "\n    WHERE slugify(value) LIKE {}"; params += [search_full]

        sql += "\n) s"
        sql += "\nWHERE rown = 1 LIMIT %d" % (limit - len(all_results),)
        
        results = execute_as_dicts(SQL(sql).format(*params))
        for result in results:
            all_results.append(result)

    return all_results
