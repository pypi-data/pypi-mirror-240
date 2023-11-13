from django.apps import AppConfig
from django.db.models.signals import post_init, post_migrate


class CmdbaseAppConfig(AppConfig):
    name = 'cmdbase'
    label = 'cmdbase'

    def ready(self):
        from .signal_handlers import on_post_init, on_post_migrate
        post_init.connect(on_post_init)
        post_migrate.connect(on_post_migrate, sender=self)
