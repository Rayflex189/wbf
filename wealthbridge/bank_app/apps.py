from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import execute_from_command_line
from django.db.utils import OperationalError, ProgrammingError
import sys


class BankAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bank_app'

    def ready(self):
        # Skip auto superuser creation during collectstatic or non-migration commands
        if 'collectstatic' in sys.argv or 'makemigrations' in sys.argv:
            return

        User = get_user_model()
        try:
            if not User.objects.filter(email=settings.SUPERUSER_EMAIL).exists():
                User.objects.create_superuser(
                    username=settings.SUPERUSER_USERNAME,
                    email=settings.SUPERUSER_EMAIL,
                    password=settings.SUPERUSER_PASSWORD
                )
        except (OperationalError, ProgrammingError):
            # Handle initial setup where DB might not yet exist or be ready
            pass
