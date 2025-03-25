from django.apps import AppConfig

class CrimeStatsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "crimestats"

    def ready(self):
        import crimestats.signals  # Import signals here
