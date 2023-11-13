"""
Imported in models.
"""
from __future__ import annotations
import logging
from typing import Any, Iterable, Sequence, TypeVar, Generic, TYPE_CHECKING
from copy import deepcopy
from django.db import connection
from django.db.models import Model
from psycopg.sql import SQL, Identifier
from zut import _UNSET

if TYPE_CHECKING:
    from .models import Item as _Item

logger = logging.getLogger(__name__)

def historize(model: type[T_Model] = None, *, at: str = None, flatten: str = None, ignore: Sequence[str]|str = None):
    """
    A decorator to indicate that a model must be historized.
    """
    def register(model):
        history = HistoryManager(model, at=at, flatten=flatten, ignore=ignore)
        historize.registered[model] = history
    
    if model is not None: # decorator used without arguments
        register(model)
        return model
    
    else: # decorator used with arguments
        def decorator(model):
            register(model)
            return model

        return decorator

historize.registered: dict[type[Model],HistoryManager] = {}


T_Model = TypeVar('T_Model', bound=Model)

class HistoryManager(Generic[T_Model]):
    def __init__(self, model: type[T_Model], *, at: str = None, flatten: str = None, ignore: Sequence[str]|str = None):
        self.model = model
        self.flatten_attname = flatten
        self.ignore_attnames = [] if ignore is None else [ignore] if isinstance(ignore, str) else ignore


    def get_snapshot(self, instance: T_Model):
        snapshot = {}
        for attname, value in instance.__dict__.items():
            if self.is_ignored(attname) or attname == self.flatten_attname:
                continue
            snapshot[attname] = deepcopy(value)

        if self.flatten_attname:
            flatten = getattr(instance, self.flatten_attname)
            if flatten is not None:
                for key, value in flatten.items():
                    if not key in snapshot:
                        snapshot[key] = value

        return snapshot
   

    def is_ignored(self, attname: str):
        if attname.startswith('_'):
            return True
        if attname in self.ignore_attnames:
            return True
        return False


class ItemDataManager:
    def __init__(self, item: _Item):
        self.item = item

    def encode(self, data: Any = None, path: str = None) -> tuple[Any, list[DiscoveredRelation]]:
        from .models import Item

        relations = []

        def _encode(value, path: str):
            if isinstance(value, dict):
                return _encode_dict(value, path)
            elif isinstance(value, list):
                return _encode_list(value, path)
            elif isinstance(value, Item):
                if not value.id:
                    raise ValueError(f"Cannot encode item {value}: id not set")
                relations.append(DiscoveredRelation(path, value.id))
                return {"_i": value.id}
            else:
                return value

        def _encode_dict(obj: dict, path: str):
            if '_i' in obj and len(obj) == 1:
                item_id = obj['_i']
                if not isinstance(item_id, int):
                    raise IssueError.invalid_type(f'"_i" ({item_id})', type(item_id), int, context={'path': path, 'obj': obj})
                if not Item.objects.filter(id=item_id).exists():
                    raise IssueError.item_not_found_with_id(item_id, context={'path': path, 'obj': obj})
                relations.append(DiscoveredRelation(path, item_id))
                return obj
            else:
                result = {}
                for key, value in obj.items():
                    result[key] = _encode(value, f"{path}.{key}" if path else key)
                return result

        def _encode_list(obj: list, path: str):
            result = []
            for i, value in enumerate(obj):
                result.append(_encode(value, f"{path}[{i}]"))
            return result
        
        if data is None:        
            return _encode(self.item.data, path), relations
        else:
            return _encode(data, path), relations


    def decode(self, path: str = None, default = _UNSET) -> dict:
        from .models import Item

        def _decode(value):
            if isinstance(value, dict):
                return _decode_dict(value)
            elif isinstance(value, list):
                return _decode_list(value)
            else:
                return value

        def _decode_dict(obj: dict):
            if '_i' in obj and len(obj) == 1:
                item_id = obj['_i']
                try:
                    return Item.objects.get(id=item_id)
                except Item.DoesNotExist:
                    return obj            
            else:
                result = {}
                for key, value in obj.items():
                    result[key] = _decode(value)
                return result

        def _decode_list(obj: list):
            result = []
            for value in obj:
                result.append(_decode(value))
            return result

        if path is None:
            return _decode(self.item.data)
        else:
            data = self.item.data
            for part in path.split('.'):
                if default is not _UNSET and not part in data:
                    return default
                data = data[part]
            return _decode(data)
        

    def set(self, path: str, value):
        data = self.item.data

        parts = path.split('.')
        for i in range(0, len(parts)):
            part = parts[i]
            if i == len(parts) - 1:
                data[part] = value
            else:
                if not part in data:
                    data[part] = {}
                data = data[part]
        

    def update_relations(self, relations: list[DiscoveredRelation]):
        from .models import Relation

        logger.debug("%s relations from item %s", len(relations), self.item)

        if not relations:
            sql = "DELETE FROM {} WHERE source_id = {}"
            params = [Identifier(Relation._meta.db_table), self.item.id]

        else:
            values_sql, values_params = self._get_discoveredrelation_values_sql(relations)

            params = []
            sql =    "WITH tmp_upsert AS ("
            sql += "\n    INSERT INTO {} (source_id, path, target_id)"; params += [Identifier(Relation._meta.db_table)]
            sql += "\n    SELECT {}, s.path, s.target_id"; params += [self.item.id]
            sql += "\n    FROM (%s) s (path, target_id)" % (values_sql,); params += values_params
            sql += "\n    ON CONFLICT (source_id, path)"
            sql += "\n    DO UPDATE SET source_id = EXCLUDED.source_id"
            sql += "\n    RETURNING id"
            sql += "\n)"
            sql += "\nDELETE FROM {}"; params += [Identifier(Relation._meta.db_table)]
            sql += "\nWHERE source_id = {} AND id NOT IN (SELECT id FROM tmp_upsert)"; params += [self.item.id]

        with connection.cursor() as cursor:
            cursor.execute(SQL(sql).format(*params))


    @classmethod
    def _get_discoveredrelation_values_sql(cls, iterable: Iterable[DiscoveredRelation]):
        query = "VALUES"
        params = []

        for i, relation in enumerate(iterable):
            if i > 0:
                query += ', '
            query += "({}, {})"
            params += [relation.path, relation.target_id]

        return query, params


class DiscoveredRelation:
    def __init__(self, path: str, target_id: int) -> None:
        self.path = path
        self.target_id = target_id
