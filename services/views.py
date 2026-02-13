from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from services.models import Service


class ServiceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список услуг"""
    permission_required = 'services.view_service'
    model = Service
    template_name = 'services/products-list.html'
    context_object_name = 'products'


class ServiceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание услуги"""
    permission_required = 'services.add_service'
    model = Service
    template_name = 'services/products-create.html'
    fields = ('title', 'description', 'price')
    success_url = reverse_lazy('services:products-list')


class ServiceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Удаление услуги"""
    permission_required = 'services.delete_service'
    model = Service
    template_name = 'services/products-delete.html'
    success_url = reverse_lazy('services:products-list')


class ServiceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Детали услуги"""
    permission_required = 'services.view_service'
    model = Service
    template_name = 'services/products-detail.html'
    context_object_name = 'products'


class ServiceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование данных услуги"""
    permission_required = 'services.change_service'
    model = Service
    template_name = 'services/products-edit.html'
    fields = ('title', 'description', 'price')

    def get_success_url(self):
        return reverse('services:products-detail', kwargs={'pk': self.object.pk})
