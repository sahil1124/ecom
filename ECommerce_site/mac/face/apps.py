from django.apps import AppConfig


class FaceConfig(AppConfig):
    name = 'face'

    def ready(self):
        import face.signals
