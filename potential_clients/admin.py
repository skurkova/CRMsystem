from django.contrib import admin

from potential_clients.models import PotentialClient


@admin.register(PotentialClient)
class PotentialClientAdmin(admin.ModelAdmin):
    """Админка потенциального клиента (лида)"""
    list_display = ('id', 'last_name', 'first_name', 'phone', 'email', 'advertising_campaign', 'created_at')
    list_display_links = ('id', 'last_name', 'first_name', 'advertising_campaign')
    search_fields = ('id', 'fullname', 'advertising_campaign__title')
    list_filter = ('advertising_campaign__title', 'created_at')
    ordering = ('id', '-created_at')
