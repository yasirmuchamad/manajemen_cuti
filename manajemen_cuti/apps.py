from django.apps import AppConfig


class ManajemenCutiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manajemen_cuti'

    def ready(self):
        import manajemen_cuti.signals