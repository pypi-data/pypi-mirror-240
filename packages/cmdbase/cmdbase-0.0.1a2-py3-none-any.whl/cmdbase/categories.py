"""
Manage categories.
"""
import os
from typing import Sequence
from django.db import connection
import yaml
import logging
from django.db.models import Choices, QuerySet
from psycopg.sql import SQL, Identifier, Literal

from .models import Category, Item, Prop, PropNature, PropIndexConfig
from .commons import filter_accessible_queryset
from .utils import skip_bom, get_jsonb_sql

logger = logging.getLogger(__name__)


def get_accessible_categories(request) -> QuerySet[Category]:
    return filter_accessible_queryset(request, Category.objects)


def update_prop_index(prop: Prop, index: str|None, index_with: Sequence[str]|None):
    index_name = f"cmdbase_prop_index_{prop.pk}"

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT indexdef FROM pg_indexes WHERE schemaname = 'public' AND indexname = '{index_name}'")
        result = cursor.fetchone()
        current_def = result[0] if result else None
        
        if index:
            new_def = "CREATE"
            if PropIndexConfig.UNIQUE.value in index:
                new_def += " UNIQUE"
            new_def += f" INDEX {index_name} ON public.cmdbase_item USING btree ("
            new_def += f"({get_jsonb_sql('data', prop.fullname, normalize=True).as_string(connection.connection)})"
            if index_with:
                for other_fullname in sorted(index_with):
                    new_def += f", COALESCE({get_jsonb_sql('data', other_fullname).as_string(connection.connection)}, 'null'::jsonb)"
            new_def += ")"

            if PropIndexConfig.FOR_CATEGORY.value in index:
                new_def += f" WHERE category_id = {prop.category_id}"

            if not current_def:
                logger.info(f"create index {index_name} for prop {prop}")
                cursor.execute(new_def)
            
            elif new_def != current_def:
                logger.info(f"replace index {index_name} for prop {prop}")
                logger.debug("drop %s: %s", index_name, current_def)
                cursor.execute(f"DROP INDEX {index_name}")
                logger.debug("create %s: %s", index_name, new_def)
                cursor.execute(new_def)

        else:
            if current_def:
                logger.info(f"drop index {index_name} for prop {prop}")
                cursor.execute(f"DROP INDEX {index_name}")


def import_categories_file(yaml_file: os.PathLike, *, overwrite= False):
    with open(yaml_file, 'r', encoding='utf-8') as fp:
        skip_bom(fp)
        documents = [c for c in yaml.safe_load_all(fp)]
    
    if len(documents) != 1:
        raise ValueError(f"yaml file {yaml_file} has {len(content)} root document, expected 1")
    content = documents[0]
    
    return import_categories(content, overwrite=overwrite)


def import_categories(content: dict, *, overwrite = False):
    """
    Import categories from the given dictionnary.
    """
    category_count = 0

    def fetch_category(name: str, obj: dict, parent: Category):
        nonlocal category_count
        category_count += 1

        need_save = False
        create = False
        try:
            category = Category.objects.get(name=name)
            if category.parent != parent:
                raise ValueError(f"Invalid parent for category {name}: {parent}, expected {category.parent}")
                
        except Category.DoesNotExist:
            category = Category(name=name, parent=parent)
            need_save = True
            create = True

        def update_field(field_name: str):
            in_obj = field_name in obj
            if value := obj.pop(field_name, None):
                existing = getattr(category, field_name)
                if existing is None or (overwrite and in_obj and value != existing):
                    setattr(category, field_name, value)
                    return True
            return need_save
        
        need_save = update_field('help')

        if need_save:
            category.save()
            
            if create:
                logger.info(f"created category {category}")

        if props := obj.pop('props', None):
            for name, prop_obj in props.items():
                fetch_prop(name, prop_obj if prop_obj is not None else {}, category)
            
        children = obj.pop('children', None)
        if obj:
            logger.warning(f"content for category {category} has unexpected keys: {', '.join(obj.keys())}")
        
        if children:
            for name, child_obj in children.items():
                fetch_category(name, child_obj if child_obj is not None else {}, category)


    def fetch_prop(name: str, obj: dict, category: Category, parent: Prop = None, parent_fullname: str = None):
        fullname = f"{parent_fullname}.{name}" if parent_fullname else name
        need_save = False
        create = False
        try:
            prop = category.directprop_set.get(parent=parent, name=name)
        except Prop.DoesNotExist:
            prop = Prop(category=category, parent=parent, name=name)
            need_save = True
            create = True


        def update_field(field_name: str, *, target_type: type = None):
            nonlocal need_save

            if not field_name in obj:
                return
            
            # Determine actual value
            raw_value = obj.pop(field_name)

            if target_type == PropIndexConfig:
                parts = []
                for part in raw_value.split(' '):
                    part = part.strip()
                    try:
                        part = target_type[part]
                        parts.append(part.value)
                    except KeyError:
                        logger.warning(f"prop {fullname} ({category.name}) has invalid index configuration: \"{part}\"")
                if parts:
                    value = ''.join(sorted(parts))
                else:
                    value = PropIndexConfig.DEFAULT.value

            elif target_type and issubclass(target_type, Choices):
                value = target_type[raw_value]

            elif target_type == list:
                value = raw_value if isinstance(raw_value, list) else [raw_value]

            else:
                value = raw_value

            # Set attribute if required
            if create:
                setattr(prop, field_name, value)
                return

            existing = getattr(prop, field_name)
            if existing is None or (overwrite and value != existing):
                setattr(prop, field_name, value)
                need_save = True
                return
    

        children = obj.pop('children', None)

        update_field('ordinal')
        update_field('nature', target_type=PropNature)
        update_field('unit')
        update_field('index', target_type=PropIndexConfig)
        update_field('index_with', target_type=list)
        update_field('search')
        update_field('help')

        if need_save:
            prop.save()

            if create:
                logger.info(f"created prop {fullname} ({category.name})")
            
        if obj:
            logger.warning(f"content for prop {fullname} ({category.name}) has unexpected keys: {', '.join(obj.keys())}")
        
        if children:
            for name, child_obj in children.items():
                fetch_prop(name, child_obj if child_obj is not None else {}, category, prop, fullname)
    
    # ---------------------------------
    # Main
    #
    if not isinstance(content, dict):
        raise TypeError(f"content: {type(content).__name__}, expected dict")
    
    if not Category.ROOT_NAME in content:
        raise ValueError(f"root category is named {list[content.keys()][0]}, expected {Category.ROOT_NAME}")
    
    fetch_category(Category.ROOT_NAME, content[Category.ROOT_NAME], None)

    logger.info(f"handled categories: {category_count}")
