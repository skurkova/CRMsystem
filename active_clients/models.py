from django.db import models

from potential_clients.models import PotentialClient
from contracts.models import Contract


class ActiveClient(models.Model):
    """Активный клиент"""
    potential_client = models.OneToOneField(PotentialClient, on_delete=models.CASCADE)
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    activated_at = models.DateTimeField(auto_now_add=True)
