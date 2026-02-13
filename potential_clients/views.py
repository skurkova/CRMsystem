from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import reverse

from potential_clients.models import PotentialClient


class PotentialClientsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список потенциальных клиентов"""
    permission_required = 'potential_clients.view_potentialclient'
    model = PotentialClient
    template_name = 'potential_clients/leads-list.html'
    context_object_name = 'leads'


class PotentialClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание потенциального клиента"""
    permission_required = 'potential_clients.add_potentialclient'
    model = PotentialClient
    template_name = 'potential_clients/leads-create.html'
    fields = ('last_name', 'first_name', 'phone', 'email', 'advertising_campaign')
    success_url = reverse_lazy('potential_clients:leads-list')


class PotentialClientsDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Детали потенциального клиента"""
    permission_required = 'potential_clients.view_potentialclient'
    model = PotentialClient
    template_name = 'potential_clients/leads-detail.html'


class PotentialClientsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Изменение данных потенциального клиента"""
    permission_required = 'potential_clients.change_potentialclient'
    model = PotentialClient
    template_name = 'potential_clients/leads-edit.html'
    fields = ('last_name', 'first_name', 'phone', 'email', 'advertising_campaign')

    def get_success_url(self):
        return reverse('potential_clients:leads-detail', kwargs={'pk': self.object.pk})


class PotentialClientsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Удаление потенциального клиента"""
    permission_required = 'potential_clients.delete_potentialclient'
    model = PotentialClient
    template_name = 'potential_clients/leads-delete.html'
    success_url = reverse_lazy('potential_clients:leads-list')
