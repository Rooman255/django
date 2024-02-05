from datetime import *
from django.utils import timezone

from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Create user."


    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com', phone='00000000000', address="Москва", registration_date=timezone.now())
        client.save()
        self.stdout.write(f'{client}')
