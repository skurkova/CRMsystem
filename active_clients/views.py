from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from active_clients.models import ActiveClient


class ActiveClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список активных клиентов"""
    permission_required = 'active_clients.view_activeclient'
    queryset = ActiveClient.objects.select_related('potential_client')
    template_name = 'active_clients/customers-list.html'
    context_object_name = 'customers'


class ActiveClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание активного клиента"""
    permission_required = 'active_clients.add_activeclient'
    model = ActiveClient
    template_name = 'active_clients/customers-create.html'
    fields = ('potential_client', 'contract')
    success_url = reverse_lazy('active_clients:customers-list')


class ActiveClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Детали активного клиента"""
    permission_required = 'active_clients.view_activeclient'
    model = ActiveClient
    template_name = 'active_clients/customers-detail.html'


class ActiveClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование данных активного клиента"""
    permission_required = 'active_clients.change_activeclient'
    model = ActiveClient
    template_name = 'active_clients/customers-edit.html'
    fields = ('potential_client', 'contract')

    def get_success_url(self):
        return reverse('active_clients:customers-detail', kwargs={'pk': self.object.pk})


class ActiveClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Удаление активного клиента"""
    permission_required = 'active_clients.delete_activeclient'
    model = ActiveClient
    template_name = 'active_clients/customers-delete.html'
    success_url = reverse_lazy('active_clients:customers-list')
