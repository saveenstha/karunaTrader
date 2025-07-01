from django.apps import AppConfig


class KtradersappConfig(AppConfig):
    name = 'mainapp'
    app_name = 'mainapp'

def ready(self):
    import signals  # This activates your signal
