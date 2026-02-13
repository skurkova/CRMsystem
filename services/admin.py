from django.contrib import admin

from services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Админка услуги"""
    list_display = ('id', 'title', 'description', 'price', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description')
    list_filter = ('price', 'created_at')
    ordering = ('id', '-created_at')
