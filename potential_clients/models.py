from django.db import models

from advertising_campaigns.models import AdvertisingCampaign


class PotentialClient(models.Model):
    """Потенциальный клиент (лид)"""
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=15)
    advertising_campaign = models.ForeignKey(AdvertisingCampaign, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
