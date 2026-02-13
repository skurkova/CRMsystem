from django.urls import path

from active_clients.views import (
    ActiveClientListView,
    ActiveClientCreateView,
    ActiveClientDetailView,
    ActiveClientUpdateView,
    ActiveClientDeleteView
)


app_name = 'active_clients'

urlpatterns = [
    path('', ActiveClientListView.as_view(), name='customers-list'),
    path('new/', ActiveClientCreateView.as_view(), name='customers-create'),
    path('<int:pk>/', ActiveClientDetailView.as_view(), name='customers-detail'),
    path('<int:pk>/edit/', ActiveClientUpdateView.as_view(), name='customers-edit'),
    path('<int:pk>/delete/', ActiveClientDeleteView.as_view(), name='customers-delete'),
]
