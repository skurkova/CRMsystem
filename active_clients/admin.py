from django.contrib import admin

from active_clients.models import ActiveClient


@admin.register(ActiveClient)
class ActiveClientAdmin(admin.ModelAdmin):
    """Админка активного клиента"""
    list_display = ('id', 'potential_client', 'contract', 'activated_at')
    list_display_links = ('id', 'potential_client')
    search_fields = ('id', 'potential_client__fullname', 'contract')
    list_filter = ('activated_at',)
    ordering = ('id', '-activated_at')
