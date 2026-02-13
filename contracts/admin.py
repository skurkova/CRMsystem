from django.contrib import admin

from contracts.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Админка контракта"""
    list_display = ('id', 'title', 'service', 'document', 'date_start', 'date_end', 'amount')
    list_display_links = ('id', 'title', 'service')
    search_fields = ('id', 'title', 'service__title')
    list_filter = ('service__title', 'date_start')
    ordering = ('id', '-date_start')
