from django.contrib import admin

from advertising_campaigns.models import AdvertisingCampaign


@admin.register(AdvertisingCampaign)
class AdvertisingCampaignAdmin(admin.ModelAdmin):
    """Админка рекламной компании"""
    list_display = ('id', 'title', 'service', 'promotion_channel', 'budget', 'created_at')
    list_display_links = ('id', 'title', 'service', 'promotion_channel')
    search_fields = ('id', 'title', 'service__title', 'promotion_channel')
    list_filter = ('service__title', 'promotion_channel')
    ordering = ('id', '-created_at')
