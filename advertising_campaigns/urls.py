from django.urls import path

from advertising_campaigns.views import (
    AdvertisingCampaignListView,
    AdvertisingCampaignCreateView,
    AdvertisingCampaignStatisticListView,
    AdvertisingCampaignUpdateView,
    AdvertisingCampaignDetailView,
    AdvertisingCampaignDeleteView
)


app_name = 'advertising_campaigns'

urlpatterns = [
    path('', AdvertisingCampaignListView.as_view(), name='ads-list'),
    path('new/', AdvertisingCampaignCreateView.as_view(), name='ads-create'),
    path('statistic/', AdvertisingCampaignStatisticListView.as_view(), name='ads-statistic'),
    path('<int:pk>', AdvertisingCampaignDetailView.as_view(), name='ads-detail'),
    path('<int:pk>/edit/', AdvertisingCampaignUpdateView.as_view(), name='ads-edit'),
    path('<int:pk>/delete/', AdvertisingCampaignDeleteView.as_view(), name='ads-delete'),
]
