from django.apps import AppConfig


class RomanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'romance'
    
    def ready(self):
        import romance.signals  # Importar signals al iniciar la aplicación
