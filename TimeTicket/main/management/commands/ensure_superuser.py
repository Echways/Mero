import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        enabled = os.environ.get("CREATE_SUPERUSER", "false").lower() == "true"
        if not enabled:
            return

        username = os.environ.get("SUPERUSER_USERNAME")
        email = os.environ.get("SUPERUSER_EMAIL")
        password = os.environ.get("SUPERUSER_PASSWORD")

        if not username or not email or not password:
            return

        user_model = get_user_model()
        if user_model.objects.filter(username=username).exists():
            return

        user_model.objects.create_superuser(username=username, email=email, password=password)
