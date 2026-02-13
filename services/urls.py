from django.urls import path

from services.views import ServiceListView, ServiceCreateView, ServiceDeleteView, ServiceUpdateView, ServiceDetailView


app_name = 'services'

urlpatterns = [
    path('', ServiceListView.as_view(), name='products-list'),
    path('new/', ServiceCreateView.as_view(), name='products-create'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='products-detail'),
    path('<int:pk>/delete/', ServiceDeleteView.as_view(), name='products-delete'),
    path('<int:pk>/edit/', ServiceUpdateView.as_view(), name='products-edit'),
]
