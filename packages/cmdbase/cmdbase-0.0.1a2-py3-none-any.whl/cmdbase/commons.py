"""
General CMDBase-related features used in several places.
"""
from typing import Any, Mapping, Sequence, TypeVar
from django.db import connection
from django.db.models import Model, QuerySet
from django.conf import settings
from django.http import HttpRequest

T_Model = TypeVar('T_Model', bound=Model)

CMDBASE_DEFAULT_AUTHORIZATION = getattr(settings, 'CMDBASE_DEFAULT_AUTHORIZATION', 'authenticated')
CMDBASE_REPORTER_GROUP = getattr(settings, 'CMDBASE_REPORTER_GROUP', 'Reporter')


def should_authenticate():
    return CMDBASE_DEFAULT_AUTHORIZATION != 'anonymous'


def filter_accessible_queryset(request: HttpRequest, queryset: QuerySet[T_Model]) -> QuerySet[T_Model]:    
    if CMDBASE_DEFAULT_AUTHORIZATION == 'staff':
        if request.user.is_staff:
            return queryset
        else:
            return queryset.none()
    
    elif CMDBASE_DEFAULT_AUTHORIZATION == 'authenticated':
        if request.user.is_authenticated:
            return queryset
        else:
            return queryset.none()
        
    elif CMDBASE_DEFAULT_AUTHORIZATION == 'anonymous':
        return queryset
    
    else:
        return request.user.is_authenticated and request.user.groups.filter(name=CMDBASE_DEFAULT_AUTHORIZATION).exists()
    

def can_search_items(request: HttpRequest):
    if CMDBASE_DEFAULT_AUTHORIZATION == 'staff':
        return request.user.is_staff
    
    elif CMDBASE_DEFAULT_AUTHORIZATION == 'authenticated':
        return request.user.is_authenticated
        
    elif CMDBASE_DEFAULT_AUTHORIZATION == 'anonymous':
        return True
    
    else:
        return request.user.is_authenticated and request.user.groups.filter(name=CMDBASE_DEFAULT_AUTHORIZATION).exists()
    

def can_report_items(request: HttpRequest):
    if CMDBASE_DEFAULT_AUTHORIZATION == 'staff':
        return request.user.is_staff
    
    else:
        if request.user.is_staff:
            return True
        return request.user.is_authenticated and CMDBASE_REPORTER_GROUP and request.user.groups.filter(name=CMDBASE_REPORTER_GROUP).exists()


def execute_as_dicts(sql: str, params: Sequence|Mapping = None) -> list[dict[str,Any]]:
    results = []

    with connection.cursor() as cursor:
        cursor.execute(sql, params=params)
        columns = [info[0] for info in cursor.description]
        for row in cursor:
            results.append({column: row[i] for i, column in enumerate(columns)})

    return results
