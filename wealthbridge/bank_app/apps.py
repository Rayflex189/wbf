from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate

def create_superuser(sender, **kwargs):
    User = get_user_model()
    try:
        if not User.objects.filter(email=settings.SUPERUSER_EMAIL).exists():
            User.objects.create_superuser(
                username=settings.SUPERUSER_USERNAME,
                email=settings.SUPERUSER_EMAIL,
                password=settings.SUPERUSER_PASSWORD
            )
    except (OperationalError, ProgrammingError):
        pass

class BankAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bank_app'

    def ready(self):
        post_migrate.connect(create_superuser, sender=self)
