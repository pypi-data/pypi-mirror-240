import logging
from importlib import import_module
from argparse import ArgumentParser
import os
import re
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from cmdbase.models import ReportOrigin
from cmdbase.categories import import_categories_file
from cmdbase.reports import report_file

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import categories or report items from the given files."
    
    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('files', nargs='+')
        parser.add_argument('--by', default='seeder')
        parser.add_argument('--origin', type=ReportOrigin, default=ReportOrigin.CODE)


    def handle(self, files: list[str], by: str, origin: ReportOrigin, **kwargs):
        by_user = None

        def handle_file(file: str):
            nonlocal by_user

            file = expand_input(file)
            lower = file.lower()

            if lower.endswith(('.yaml','.yml')):
                logger.info(f"import categories from {file}")
                import_categories_file(file)
            
            elif lower.endswith(('.json', '.jsonc')):
                logger.info(f"import items from {file}")
                if by_user is None:
                    by_user, created = get_user_model().objects.get_or_create(username=by)
                    if created:
                        logger.info(f"created user \"{by_user.get_username()}\"")
                report_file(file, by=by_user, origin=origin)
            
            elif m := re.match(r'^(?P<file_without_ext>.+)\.py(?:\:(?P<func>[a-z0-9_]+))?$', file, re.I):
                module_name = ''
                for part in m['file_without_ext'].replace('\\', '/').split('/'):
                    if part == '.':
                        continue
                    elif part == '..':
                        logger.error(f"python file path cannot contain '..': {file}")
                        return
                    module_name += ('.' if module_name else '') + part

                func_name = m['func']
                
                logger.info(f"exec {f'{func_name} from ' if func_name else ''}module {module_name} (from file {file})")
                module = import_module(module_name)

                if func_name:
                    func = getattr(module, func_name)
                    func()

            else:
                logger.error(f"don't know how to import {file}")

        for file in files:
            handle_file(file)


def expand_input(path: str) -> str:
    path = os.path.expanduser(path)
    if m := re.match(r'^@(?P<module>[a-z0-9_\.]+)/(?P<path>.+)$', path):
        module = import_module(m['module'])
        path = os.path.join(os.path.dirname(module.__file__), m['path'])
    return path
