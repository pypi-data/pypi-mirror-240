from __future__ import annotations
import logging
import os
from types import ModuleType
from django.apps import AppConfig
from django.conf import settings
from django.db import connection
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management import call_command
from django.db import models
from django.db.models import Model
from django.utils import timezone
from psycopg.sql import SQL, Composable, Identifier, Literal
from importlib import import_module

from zut.db import PgAdapter
from .models import Category
from .bases import historize
from .commons import CMDBASE_REPORTER_GROUP

logger = logging.getLogger(__name__)


def on_post_init(sender: type[Model], instance: Model, **kwargs):
    if history := historize.registered.get(sender, None):
        instance._history_snapshot = history.get_snapshot(instance)


def on_post_migrate(sender: AppConfig, **kwargs):
    if not Category.objects.filter(parent=None).exists():
        logger.info(f"create root category \"{Category.ROOT_NAME}\"")
        Category.objects.create(name=Category.ROOT_NAME, parent=None)

    deploy_table_defaults(sender)
    deploy_choices_tables()

    if CMDBASE_REPORTER_GROUP:
        reporter_group, created = Group.objects.get_or_create(name=CMDBASE_REPORTER_GROUP)
        if created:
            logger.info(f"created group {reporter_group.name}")
    
    if settings.DEBUG:
        deploy_dev_superuser()

    run_module_seed('seed_cmdbase', ignore_not_found=True)


def deploy_table_defaults(sender: AppConfig):
    # TODO/ROADMAP: with Django 5.0, use db_default in Model classes (instead of this function)

    def deploy(model: models.Model, field: models.Field, value: Composable):
        db_column = field.db_column or field.name

        logger.debug("set default value for %s.%s", model._meta.db_table, db_column)
        with connection.cursor() as cursor:
            cursor.execute(SQL("ALTER TABLE {table} ALTER COLUMN {column} SET DEFAULT {value}").format(table=Identifier(model._meta.db_table), column=Identifier(db_column), value=value))


    for model in sender.get_models():
        field: models.Field
        for field in model._meta.fields:
            if not field.null:
                if isinstance(field, models.BooleanField) and isinstance(field.default, bool):
                    deploy(model, field, Literal(field.default))
                elif isinstance(field, models.IntegerField) and isinstance(field.default, int):
                    deploy(model, field, Literal(field.default))
                elif isinstance(field, models.DateField) and (field.default == timezone.now or field.auto_now or field.auto_now_add):
                    deploy(model, field, SQL('now()'))


def deploy_choices_tables():
    with PgAdapter(connection) as db:
        db.deploy_choices_table()


def deploy_dev_superuser():
    os.environ.setdefault('DJANGO_SUPERUSER_USERNAME', 'admin')
    os.environ.setdefault('DJANGO_SUPERUSER_EMAIL', 'admin@localhost')
    os.environ.setdefault('DJANGO_SUPERUSER_PASSWORD', 'admin')
    
    username = os.environ['DJANGO_SUPERUSER_USERNAME']
    if not get_user_model().objects.filter(username=username).exists():
        logger.info(f"create super user \"{username}\"")
        call_command('createsuperuser', interactive=False)

    
def run_module_seed(module: str|ModuleType, ignore_not_found = False):
    if isinstance(module, str):
        try:
            module = import_module(module)
        except ModuleNotFoundError as err:
            if ignore_not_found and err.name == module:
                logger.debug(f"module {err.name} not found")
                return
            else:
                raise

    logger.info(f"run {module.__name__}.seed")
    func = getattr(module, "seed")
    func()
