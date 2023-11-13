"""
General utilities used by CMDBase but not directly linked to it.

NOTE: Cannot use:
- Apps specifics such as models
- Django utils that require apps to be loaded, such as django.contrib.auth.mixins.UserPassesTestMixin
"""
from __future__ import annotations

from datetime import date, datetime
import inspect
import os
import re
from pathlib import Path
from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.migrations import RunSQL
from psycopg.sql import SQL, Identifier
from zut import skip_bom

class NoPastDateValidator:
    message = _("Date cannot be in the past.")
    code = "invalid"
    
    def __call__(self, value):        
        if isinstance(value, datetime):
            if value < timezone.now():
                raise forms.ValidationError(self.message, code=self.code, params={"value": value})
        
        elif isinstance(value, date):
            if value < timezone.now().today():
                raise forms.ValidationError(self.message, code=self.code, params={"value": value})
    

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
 
 
class DateTimeLocalField(forms.DateTimeField):
    # See: https://stackoverflow.com/a/69965027
    #
    # Set DATETIME_INPUT_FORMATS here because, if USE_L10N 
    # is True, the locale-dictated format will be applied 
    # instead of settings.DATETIME_INPUT_FORMATS.
    # See also: 
    # https://developer.mozilla.org/en-US/docs/Web/HTML/Date_and_time_formats
    #
     
    input_formats = [
        "%Y-%m-%dT%H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S.%f", 
        "%Y-%m-%dT%H:%M"
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")


# -----------------------------------------------------------------------------
# region SQL
#

def get_jsonb_sql(column: str, path: str, *, as_text = False, normalize = False):
    params = []

    if re.match(r'^[0-9a-z_\.]+$', column):
        sql = column
    else:
        sql = "{}"
        params.append(Identifier(column))

    parts = path.split('.')

    for i in range(0, len(parts)):        
        if as_text and i == len(parts) - 1:
            operator = '->>'
        else:
            operator = '->'

        if normalize:
            sql = "(%s %s {}::text)" % (sql, operator)
        else:
            sql = "%s%s{}" % (sql, operator)
        
        params.append(parts[i])

    return SQL(sql).format(*params)

# endregion


# -----------------------------------------------------------------------------
# region Migrations
#

def get_sql_migration_operations(directory: os.PathLike = None, vars: dict = None):

    def get_ordered_files(directory: os.PathLike, *, ext: str = None, recursive: bool = False) -> list[Path]:
        if not isinstance(os, Path):
            directory = Path(directory)

        if ext and not ext.startswith('.'):
            ext = f'.{ext}'

        def generate(directory: Path):
            for path in sorted(directory.iterdir(), key=lambda entry: (0 if entry.is_dir() else 1, entry.name)):
                if path.is_dir():
                    if recursive:
                        yield from generate(path)
                elif not ext or path.name.lower().endswith(ext):
                    yield path

        return [ path for path in generate(directory) ]


    def get_sql_and_reverse_sql(file: os.PathLike):
        sql = None
        reverse_sql = None

        with open(file, 'r', encoding='utf-8') as fp:
            skip_bom(fp)
            while line := fp.readline():
                if vars:
                    for name, value in vars.items():
                        line = line.replace("{"+name+"}", value)

                if reverse_sql is None:
                    # search !reverse mark
                    stripped_line = line = line.strip()
                    if stripped_line.startswith('--') and stripped_line.lstrip(' -\t').startswith('!reverse'):
                        reverse_sql = line
                    else:
                        sql = (sql + '\n' if sql else '') + line
                else:
                    reverse_sql += '\n' + line

        return sql, reverse_sql


    if directory is None:
        calling_module = inspect.getmodule(inspect.stack()[1][0])
        calling_file = Path(calling_module.__file__)
        directory = calling_file.parent.joinpath(calling_file.stem)

    operations = []

    for path in get_ordered_files(directory, ext='.sql', recursive=True):
        sql, reverse_sql = get_sql_and_reverse_sql(path)
        operations.append(RunSQL(sql, reverse_sql))

    return operations

# endregion
