from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """Создаёт суперпользователя"""

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='admin'
            )
            self.stdout.write(
                    self.style.SUCCESS(f'Суперпользователь успешно создан!')
                )
        else:
            self.stdout.write(
                self.style.WARNING(f'Суперпользователь уже существует')
            )
