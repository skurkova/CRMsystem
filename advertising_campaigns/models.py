from django.db import models

from services.models import Service


class AdvertisingCampaign(models.Model):
    """Рекламная кампания"""
    title = models.CharField(max_length=50, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    promotion_channel = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
