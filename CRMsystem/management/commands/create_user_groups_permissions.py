from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Автоматически создаёт группы пользователей с правами после миграций"""
        # Группа: Оператор (operator)
        operator_group, _ = Group.objects.get_or_create(name='operator')
        operator_permission = Permission.objects.get(codename__in=[
            'add_potentialclient',
            'change_potentialclient',
            'view_potentialclient',
            'delete_potentialclient'
        ])
        operator_group.permissions.add(operator_permission)
        operator_group.save()

        # Группа: Маркетолог (marketer)
        marketer_group, _ = Group.objects.get_or_create(name='marketer')
        marketer_permissions = Permission.objects.get(codename__in=[
            'add_service',
            'change_service',
            'view_service',
            'delete_service',
            'add_advertisingcampaign',
            'change_advertisingcampaign',
            'view_advertisingcampaign',
            'delete_advertisingcampaign',
        ])
        marketer_group.permissions.add(marketer_permissions)
        marketer_group.save()

        # Группа: Менеджер (manager)
        manager_group, _ = Group.objects.get_or_create(name='manager')
        manager_permissions = Permission.objects.get(codename__in=[
            'add_contract',
            'change_contract',
            'view_contract',
            'delete_contract',
            'view_potentialclient',
            'add_activeclient',
            'change_activeclient',
            'view_activeclient',
            'delete_activeclient',
        ])
        manager_group.permissions.add(manager_permissions)
        marketer_group.save()
