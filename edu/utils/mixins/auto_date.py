from django.db import models


class AutoDateMixin(models.Model):
    """Миксин для даты создания и изменения моделей"""
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    
    class Meta:
        abstract = True
