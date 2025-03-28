from django.apps import AppConfig

class ManifestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manifestapp'  # Must match the app folder name

    def ready(self):
        import os
        from django.conf import settings
        if os.environ.get('RUN_MAIN') == 'true' and not settings.DEBUG:
            from .scheduler import start_scheduler
            start_scheduler()
        elif settings.DEBUG:
            from .scheduler import start_scheduler
            start_scheduler()