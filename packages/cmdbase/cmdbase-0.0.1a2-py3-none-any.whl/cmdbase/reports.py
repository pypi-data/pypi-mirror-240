from __future__ import annotations
import os
from typing import Any
import jsonc
import logging
from django.contrib.auth.models import AbstractUser
from zut import slugify, skip_bom
from .models import Category, Item, Report, ReportAction, ReportItem, ReportOrigin
from .issues import IssueError

logger = logging.getLogger(__name__)


def report_content(content: dict|list, *, by: AbstractUser, origin: ReportOrigin) -> list[Report]:
    """
    Import items from the given list of dictionnaries.

    Special keys are prefixed with `_`:

    - `_c`: category. Example:
    
        ```
        {"_c": "VM", "name": "vm01"}
        ```

    - `_i`: identifier of an item. Must be the only key of the object. May be an integer or a "{category}/{name}" string. Examples:
    
        ```
        {"_i": 1234}
        {"_i": "Cluster/VMWare Cluster"}
        ```

    - `_a`: alias. When used alone, this is an alias usage. Otherwise this is an alias definition.
    
        Example of alias definition:

        ```
        {"_c": "Product", "name": "My Great Server Model", "_a": "Model1"}
        ```

        Example of alias usage:

        ```
        {"_c": "Server", "name": "sp01", "product": {"_a": "Model1"}}
        ```

    - `_k`: match with the given key(s) instead of name.

    - `_r_{relation}`: reverse relation. The described item will be added as a relation in the item pointed by the key. In the following example, "vm01" will be added in the "members" relation of "VMWare Cluster".
        
        ```
        {"_c": "VM", "name": "vm01", "_r_members": {"_c": "Cluster", "name": "VMWare Cluster"}}
    """
    
    if isinstance(content, dict):
        content = [content]
    elif not isinstance(content, list):
        raise TypeError(f"content: {type(content).__name__}, expected list or dict")

    aliases = Aliases()

    reports = []
    issue_count = 0
    item_count = 0
    created_count = 0
    updated_count = 0
    for i, obj in enumerate(content):
        report = report_single(obj, by=by, origin=origin, obj_index=i, aliases=aliases)
        reports.append(report)
        issue_count += report.issue_set.count()
        for ri in report.reportitem_set.all():
            item_count += 1
            if ri.action == ReportAction.CREATE:
                created_count += 1
            elif ri.action == ReportAction.UPDATE:
                updated_count += 1

    if aliases.unused_names:
        logger.warning(f"unused alias: {', '.join(aliases.unused_names)}")
        for unused in aliases.unused_names:
            alias = aliases.get_definition(unused)
            IssueError("Unused alias: {name}.", name=unused, on=alias.report, context=alias.context).save()            
            issue_count += 1

    logger.log(logging.WARNING if issue_count > 0 else logging.INFO, f"handled {origin.label} reports by {by.get_username()}: {len(reports)}, items: {item_count}, created: {created_count}, updated: {updated_count}, issues: {issue_count}")

    return reports


def report_file(json_file: os.PathLike, *, by: AbstractUser, origin: ReportOrigin) -> list[Report]:
    with open(json_file, 'r', encoding='utf-8') as fp:
        skip_bom(fp)
        content = jsonc.load(fp)
        
    return report_content(content, by=by, origin=origin)


def report_single(obj: dict, *, by: AbstractUser, origin: ReportOrigin, obj_index: int = None, aliases: Aliases = None) -> Report:
    if aliases is None:
        aliases = Aliases()


    report = Report.objects.create(by=by, origin=origin)


    def handle_obj(obj: dict, *, require_item: bool, path: str):
        if path is None:
            # root reportitem created ASAP so that we have data in database even in case of issue
            root_reportitem = report.reportitem_set.create(path=path, data=obj)
        else:
            root_reportitem = None

        try:
            if not isinstance(obj, dict):
                raise IssueError.invalid_type('item input', actual=type(obj), expected=dict, context={'path': path, 'obj': obj})

            if '_i' in obj:
                # identifier of item
                if len(obj) > 1:
                    raise IssueError('Key "_i" must be the only key of the object.', context={'path': path, 'obj': obj})
                
                id = obj['_i']
                if isinstance(id, int):
                    item = Item.objects.filter(id=id).first()
                    if not item:
                        raise IssueError.item_not_found_with_id(id=id, context={'path': path, 'obj': obj})
                    return item
                
                elif isinstance(id, str):
                    pos = id.find('/')
                    if not pos:
                        raise IssueError('Expected a slash in item category/slug "{category_and_slug}".', category_and_slug=id, context={'path': path, 'obj': obj})
                    category_slug = slugify(id[0:pos])
                    name_slug = slugify(id[pos+1:])
                    item = Item.objects.filter(category__slug=category_slug, slug=name_slug).first()
                    if not item:
                        raise IssueError('Item not found with category/slug "{category_and_slug}".', category_and_slug=f"{category_slug}/{name_slug}", context={'path': path, 'obj': obj})
                    return item
                
                else:
                    raise IssueError('Expected "_i" to be an integer or a string.', context={'path': path, 'obj': obj})
                
            elif '_a' in obj and len(obj) == 1:
                # usage of an alias            
                alias = obj['_a']
                return aliases.get(alias)
            
            elif '_c' in obj:
                category = obj['_c']
                name = None
                data: dict[str,Any] = {}
                matching_keys = []
                invalid_keys = []
                alias = None
                reverse_relations: dict[str,Item] = {}
                for key, value in obj.items():
                    if key == '_c':
                        pass
                    elif key == 'name':
                        name = value
                    elif key == '_k':
                        matching_keys = value if isinstance(value, list) else [value]
                    elif key == '_a':
                        alias = value
                    elif not isinstance(key, str):
                        invalid_keys.append(key)
                    elif key.startswith('_r_') and len(key) > 3:
                        if isinstance(value, list):
                            reverse_relations[key] = []
                            for i, elem in enumerate(value):
                                elem_obj = handle_obj(elem, require_item=True, path=f"{path if path else ''}{key}[{i}]")
                                reverse_relations[key].append(elem_obj)
                        else:
                            reverse_relations[key] = handle_obj(value, require_item=True, path=f"{path + '.' if path else ''}{key}")
                    elif key.startswith('_') or key in Item.invalid_data_keys():
                        invalid_keys.append(key)
                    else:
                        if isinstance(value, dict):
                            data[key] = handle_obj(value, require_item=False, path=f"{path + '.' if path else ''}{key}")
                        elif isinstance(value, list):
                            data[key] = []
                            for i, elem in enumerate(value):
                                elem_obj = handle_obj(elem, require_item=False, path=f"{path if path else ''}{key}[{i}]")
                                data[key].append(elem_obj)
                        else:
                            data[key] = value

                if invalid_keys:
                    raise IssueError('Invalid key: {name}.', name=', '.join(invalid_keys), context={'path': path, 'obj': obj})

                # Find category                        
                category_slug = slugify(category)
                category = Category.objects.filter(slug=category_slug).first()
                if not category:
                    raise IssueError('Category not found with slug {slug}.', slug=category_slug)

                category, name, data = transform_input(category, name, data)
                
                # Fetch item
                item = None
                create = False
                if matching_keys:
                    item = find_item_by_key(category, matching_keys, data)

                if not item:
                    if not name:
                        if matching_keys:
                            raise IssueError('Missing name to create item (no matching item found).', context={'path': path, 'obj': obj})
                        else:
                            raise IssueError('Missing item name.', context={'path': path, 'obj': obj})
                    item, create = fetch_item(category, name, data)

                reportitem = root_reportitem or ReportItem(report=report, path=path, data=obj)

                if create:
                    item.save(reportitem=reportitem)
                    logger.info(f"created item {item}")
                else:
                    if update_existing(item, name, data):
                        item.save(reportitem=reportitem)

                if root_reportitem and not root_reportitem.item:
                    root_reportitem.item = item
                    root_reportitem.action = ReportAction.NOCHANGE
                    root_reportitem.save()
                
                # Define alias
                if alias:
                    aliases.define(alias, item, report=report, context={'path': path, 'obj': obj})
                
                # Update reverse relations
                for key, source_item in reverse_relations.items():
                    relation = key[3:]

                    if isinstance(source_item, list):
                        for i, source in enumerate(source_item):
                            reportitem = create_relation_reportitem(obj, path, key, i)
                            add_to_relation(source, relation, item, reportitem=reportitem)
                    else:
                        reportitem = create_relation_reportitem(obj, path, key)
                        add_to_relation(source_item, relation, item, reportitem=reportitem)

                return item
            
            else:
                # not an item
                if require_item:
                    raise IssueError('Missing "_c", "_i" or "_a" key.', context={'path': path, 'obj': obj})
                elif '_k' in obj:
                    raise IssueError('Key "_k" cannot be used without key "_c".', context={'path': path, 'obj': obj})
                else:
                    result = {}
                    for key, value in obj.items():
                        if isinstance(key, str) and key.startswith('_r_'):
                            raise IssueError('Key {key}, defining a reverse relation, cannot be provided without an item identification key ("_c", "_i" or "_a").', key=key, context={'path': path, 'obj': obj})
                        
                        if isinstance(value, dict):
                            value = handle_obj(value, require_item=False, path=f"{path + '.' if path else ''}{key}")
                        elif isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
                            value = [handle_obj(sub, require_item=False, path=f"{path + '.' if path else ''}{key}[{i}]") for i, sub in enumerate(value)]

                        result[key] = value
                    return result
        
        except Exception as err:
            if isinstance(err, IssueError) and err.context:
                raise
            else:
                raise IssueError(err, context={'path': path, 'obj': obj}) from err
            

    def find_item_by_key(category: Category, keys: list[str], data: dict[str,Any]) -> Item|None:
        filter_kwargs = {'category': category}

        for key in keys:
            value = data

            for part in key.split('.'):
                if not isinstance(value, dict) or not part in value:
                    raise IssueError("Cannot match using key {key}: value not found in data.", key=key)
                value = value[part]

            if isinstance(value, Item):
                value = {"_i": value.pk}

            filter_kwargs[f"data__{key.replace('.', '__')}"] = value
        
        
        try:
            item = Item.objects.get(**filter_kwargs)
            logger.debug("found item %s by key %s", item, filter_kwargs)
            return item
        except Item.DoesNotExist:
            return None


    def fetch_item(category: Category, name: str, data: dict[str,Any]) -> Item:        
        slug = slugify(name)
        
        try:
            item = Item.objects.get(category=category, slug=slug)
            logger.debug("found item %s by name", item)
            return item, False
        except Item.DoesNotExist:
            item = Item(category=category, name=name)
            if data:
                item.data = data
            return item, True
    

    def create_relation_reportitem(target_obj: dict, target_path: str, key: dict, index: int = None):
        path = f"{target_path + '.' if target_path else ''}{key}"
        data = obj[key]

        if index is not None:
            path += f"[{index}]"
            data = data[index]

        relation_parts = key[3:].split('.')
        for relation in relation_parts:
            prev = data
            if relation in prev:
                data = prev[relation]
            else:
                data = {}
                prev[relation] = data

        if not isinstance(data, list):
            new_data = []
            if data:
                new_data.append(data)
            data = new_data
            prev[relation] = data

        data.append({'_c': target_obj['_c'], 'name': target_obj['name']})

        return ReportItem(report=report, path=path, data=data)
    

    def add_to_relation(source: Item, relation: str, target: Item, *, reportitem: ReportItem):
        if not source.data:
            source.data = {}

        existing_target = source.data_manager.decode(relation, None)
        if existing_target == target:
            return # nothing to do
        
        elif isinstance(existing_target, list) and target in existing_target:
            return # nothing to do
            
        elif existing_target:
            new_target = [existing_target] if not isinstance(existing_target, list) else existing_target
            new_target.append(target)
            target = new_target

        source.data_manager.set(relation, target)
        
        logger.debug("add to %s relation \"%s\": %s", source, relation, target)
        source.save(reportitem=reportitem)


    # ---------------------------------
    # Main
    #
    logger.debug("import %s (index: %s)", obj, obj_index)
    try:
        handle_obj(obj, require_item=True, path=None)
    except IssueError as err:
        logger.exception(f"Cannot import item{f' at index {obj_index}' if obj_index is not None else ''}")
        if not err.on:
            err.on = report
        err.save()
    
    return report


class Aliases:
    def __init__(self):
        self._aliases: dict[Any,AliasDefinition] = {}
        self._used_names: set = set()

    def define(self, name: Any, value: Item, *, report: Report, context: Any):        
        if name in self._aliases:
            del self._aliases[name]
            raise IssueError('Alias "{name}" already defined.', name=name)
        self._aliases[name] = AliasDefinition(value, report, context)

    def get(self, name: Any):    
        if not name in self._aliases:
            raise IssueError('Alias "{name}" not defined.', name=name)
        self._used_names.add(name)
        return self._aliases[name].item

    def get_definition(self, name: Any):    
        if not name in self._aliases:
            raise IssueError('Alias "{name}" not defined.', name=name)
        return self._aliases[name]
    
    @property
    def unused_names(self):
        try:
            return self._unused_names
        except:
            self._unused_names = [name for name in self._aliases if not name in self._used_names]
            return self._unused_names


class AliasDefinition:
    def __init__(self, item: Item, report: Report, context: Any):
        self.item = item
        self.report = report
        self.context = context


def transform_input(category: Category, name, data) -> tuple(Category, str, dict[str,Any]):
    # TODO/ROADMAP: use custom transform rules
    return category, name, data


def update_existing(item: Item, new_name: str, new_data: dict|None):
    """
    Return True if save is needed.
    """
    #TODO: handle new_name

    if not new_data:
        return False

    if item.data is None:
        item.data = new_data
        return True
    
    if not isinstance(item.data, dict):
        raise IssueError("Existing data for item {item} is of type {typename}, expected dict.", itemtypename=type(item.data).__name__)
    
    def update_existing_dict(existing_dict, key, new_value):
        if not key in existing_dict:
            if new_value is not None:
                existing_dict[key] = new_value
                return True
            return False

        #if not overwrite: #TODO: replace this by custom rule action
        #    return False

        if new_value is None:
            del existing_dict[key]
            return True
        
        existing_value = existing_dict[key]
        
        if isinstance(existing_value, dict) and isinstance(new_value, dict):
            need_save = False
            for key, value in new_value.items():
                if update_existing_dict(existing_value, key, value):
                    need_save = True
            return need_save

        if isinstance(new_value, Item):
            new_value = {"_i": new_value.id}

        if existing_value != new_value:
            existing_dict[key] = new_value
            return True
            
        return False
    
    need_save = False
    for key, new_value in new_data.items():
        if update_existing_dict(item.data, key, new_value):
            need_save = True
    return need_save
