from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Seeds the database with an admin user.'
    
    def handle(self, *args, **options):
      if not User.objects.filter(is_staff=True).exists():
            User.objects.create_superuser(
                 email='admin@example.com', 
                 password='AdminPassword123',
                 first_name='Admin',
                 last_name='User',
                 phone='1234567890'
            )
            self.stdout.write(self.style.SUCCESS('Admin user created successfully.'))
      else:
            self.stdout.write(self.style.WARNING('Admin user already exists.'))