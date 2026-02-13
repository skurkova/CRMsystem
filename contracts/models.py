from django.db import models

from services.models import Service


def contract_document_directory_path(instance: 'Contract', filename: str):
    """Определяем путь к каталогу документов контракта"""
    return f'contracts/contract_{instance.pk}/{filename}'


class Contract(models.Model):
    """Контракт"""
    title = models.CharField(max_length=100, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    document = models.FileField(upload_to=contract_document_directory_path)
    date_start = models.DateField()
    date_end = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.title
