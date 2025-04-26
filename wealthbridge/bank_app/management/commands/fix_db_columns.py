from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Auto create missing UserProfile fields if not exist'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Check if 'expiry_date' exists
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name='bank_app_userprofile' AND column_name='expiry_date';
            """)
            result = cursor.fetchone()

            if not result:
                self.stdout.write(self.style.WARNING('Missing "expiry_date" field. Creating...'))
                cursor.execute("""
                    ALTER TABLE bank_app_userprofile 
                    ADD COLUMN expiry_date varchar(255);
                """)
                self.stdout.write(self.style.SUCCESS('Successfully added "expiry_date" field.'))
            else:
                self.stdout.write(self.style.SUCCESS('"expiry_date" already exists. No changes needed.'))
