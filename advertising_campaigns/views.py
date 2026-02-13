from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count, Sum, F
from django.db.models.functions import Round
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from advertising_campaigns.models import AdvertisingCampaign


class AdvertisingCampaignListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список рекламных кампаний"""
    permission_required = 'advertising_campaigns.view_advertisingcampaign'
    model = AdvertisingCampaign
    template_name = 'advertising_campaigns/ads-list.html'
    context_object_name = 'ads'


class AdvertisingCampaignCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание рекламной кампании"""
    permission_required = 'advertising_campaigns.add_advertisingcampaign'
    model = AdvertisingCampaign
    template_name = 'advertising_campaigns/ads-create.html'
    fields = ('title', 'service', 'promotion_channel', 'budget')
    success_url = reverse_lazy('advertising_campaigns:ads-list')


class AdvertisingCampaignStatisticListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Статистика рекламных кампаний"""
    permission_required = 'advertising_campaigns.view_advertisingcampaign'
    model = AdvertisingCampaign
    template_name = 'advertising_campaigns/ads-statistic.html'
    context_object_name = 'ads'

    def get_queryset(self):
        queryset = AdvertisingCampaign.objects.annotate(
            leads_count=Count('potentialclient', distinct=True),
            customers_count=Count('potentialclient__activeclient', distinct=True),
            profit=Round(Sum('potentialclient__activeclient__contract__amount') / F('budget'), 2))
        return queryset


class AdvertisingCampaignDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Детали рекламной кампании"""
    permission_required = 'advertising_campaigns.view_advertisingcampaign'
    model = AdvertisingCampaign
    template_name = 'advertising_campaigns/ads-detail.html'


class AdvertisingCampaignUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование данных рекламной кампании"""
    permission_required = 'advertising_campaigns.change_advertisingcampaign'
    model = AdvertisingCampaign
    template_name = 'advertising_campaigns/ads-edit.html'
    fields = ('title', 'service', 'promotion_channel', 'budget')

    def get_success_url(self):
        return reverse('advertising_campaigns:ads-detail', kwargs={"pk": self.object.pk})


class AdvertisingCampaignDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Удаление рекламной кампании"""
    permission_required = 'advertising_campaigns.delete_advertisingcampaign'
    model = AdvertisingCampaign
    template_name = 'advertising_campaigns/ads-delete.html'
    success_url = reverse_lazy('advertising_campaigns:ads-list')
