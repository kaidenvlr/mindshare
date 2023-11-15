from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create superuser if it does not exist"

    def handle(self, *args, **options):
        if not User.objects.filter(username=settings.SUPERUSER_USERNAME):
            User.objects.create_superuser(
                username=settings.SUPERUSER_USERNAME,
                email=settings.SUPERUSER_MAIL,
                password=settings.SUPERUSER_PASSWORD
            )
            self.stdout.write(self.style.SUCCESS("Successfully created."))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exist."))