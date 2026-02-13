from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from contracts.models import Contract


class ContractListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список контрактов"""
    permission_required = 'contracts.view_contract'
    queryset = Contract.objects.select_related('service')
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'


class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание контракта"""
    permission_required = 'contracts.add_contract'
    model = Contract
    template_name = 'contracts/contracts-create.html'
    fields = ('title', 'service', 'document', 'date_start', 'date_end', 'amount')
    success_url = reverse_lazy('contracts:contracts-list')


class ContractDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Удаление контракта"""
    permission_required = 'contracts.delete_contract'
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:contracts-list')


class ContractDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Детали контракта"""
    permission_required = 'contracts.view_contract'
    model = Contract
    template_name = 'contracts/contracts-detail.html'
    context_object_name = 'contracts'


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Изменение данных контракта"""
    permission_required = 'contracts.change_contract'
    model = Contract
    template_name = 'contracts/contracts-edit.html'
    fields = ('title', 'service', 'document', 'date_start', 'date_end', 'amount')

    def get_success_url(self):
        return reverse('contracts:contracts-detail', kwargs={'pk': self.object.pk})
