from myapp.models import Client
from django.core.management.base import BaseCommand

def create_client(name, email, phone, address):
    client = Client(name=name, email=email, phone=phone, address=address)
    client.save()
    return client


def get_client(client_id):
    try:
        client = Client.objects.get(id=client_id)
        return client
    except Client.DoesNotExist:
        return None


def update_client(client_id, **kwargs):
    client = get_client(client_id)
    if client:
        for key, value in kwargs.items():
            setattr(client, key, value)
        client.save()
    return client


def delete_client(client_id):
    client = get_client(client_id)
    if client:
        client.delete()
    return client