from __future__ import annotations
from django.http import HttpRequest
from django.utils.translation import gettext as _
from zut import slugify
from .models import Category, Item

_RECENT_MAX_LENGTH = 20
_RECENTS_SESSION_KEY = 'cmdbase:recents'


def add_recent(request: HttpRequest, obj):
    if isinstance(obj, Category):
        recent = Recent(None, obj.name)
    elif isinstance(obj, Item):
        recent = Recent(obj.category.name, obj.name)
    else:
        raise TypeError(f"obj: {type(obj).__name__}")
    
    this_serialized = recent.serialize()
    recent_list = [this_serialized]
    
    if _RECENTS_SESSION_KEY in request.session:
        for serialized in request.session[_RECENTS_SESSION_KEY]:
            if serialized == this_serialized:
                continue
            
            recent_list.append(serialized)

            if len(recent_list) == _RECENT_MAX_LENGTH:
                break
    
    request.session[_RECENTS_SESSION_KEY] = recent_list


def get_recents(request: HttpRequest) -> list[Recent]:
    recents = []

    for serialized in request.session.get(_RECENTS_SESSION_KEY, []):
        try:
            recent = Recent.from_serialized(serialized)
            if recent:
                recents.append(recent)
        except:
            pass

    return recents


def clear_recents(request: HttpRequest):
    request.session.pop(_RECENTS_SESSION_KEY, None)


class Recent:
    def __init__(self, category_name: str|None, name: str):
        self.name = name
        self.category_name = category_name or None

    @property
    def category_slug(self):
        return slugify(self.category_name, if_none=None)
    
    @property
    def slug(self):
        return slugify(self.name, if_none=None)

    def serialize(self):
        return f"{self.category_name or ''}:{self.name}"

    @classmethod
    def from_serialized(cls, serialized: str):
        pos = serialized.index(':')
        category_name = serialized[0:pos]
        name = serialized[pos+1:]
        return cls(category_name, name)
