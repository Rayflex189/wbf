from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError


class BankAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bank_app'

    def ready(self):
        User = get_user_model()
        try:
            if not User.objects.filter(email=settings.SUPERUSER_EMAIL).exists():
                User.objects.create_superuser(
                    username=settings.SUPERUSER_NAME,
                    email=settings.SUPERUSER_EMAIL,
                    password=settings.SUPERUSER_PASSWORD
                )
        except (OperationalError, ProgrammingError):
            # Avoid errors during migrations or when DB isn't ready
            pass
