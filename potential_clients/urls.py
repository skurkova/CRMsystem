from django.urls import path

from potential_clients.views import (
    PotentialClientsListView,
    PotentialClientCreateView,
    PotentialClientsDetailView,
    PotentialClientsUpdateView,
    PotentialClientsDeleteView
)


app_name = 'potential_clients'

urlpatterns = [
    path('', PotentialClientsListView.as_view(), name='leads-list'),
    path('new/', PotentialClientCreateView.as_view(), name='leads-create'),
    path('<int:pk>/', PotentialClientsDetailView.as_view(), name='leads-detail'),
    path('<int:pk>/edit/', PotentialClientsUpdateView.as_view(), name='leads-edits'),
    path('<int:pk>/delete/', PotentialClientsDeleteView.as_view(), name='leads-delete'),
]
