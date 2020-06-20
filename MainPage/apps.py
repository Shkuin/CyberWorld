from django.apps import AppConfig


class MainpageConfig(AppConfig):
    name = 'MainPage'

    def ready(self):
        import MainPage.signals
