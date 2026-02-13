from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse

from services.models import Service
from advertising_campaigns.models import AdvertisingCampaign
from potential_clients.models import PotentialClient
from active_clients.models import ActiveClient


class IndexView(View):
    """Главная страница"""
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'products_count': Service.objects.count(),
            'advertisements_count': AdvertisingCampaign.objects.count(),
            'leads_count': PotentialClient.objects.count(),
            'customers_count': ActiveClient.objects.count(),
        }
        return render(request, template_name='index.html', context=context)
