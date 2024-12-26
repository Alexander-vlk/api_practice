from django.db import models
from django.contrib.auth.models import User

from utils.mixins.auto_date import AutoDateMixin


class BaseItem(AutoDateMixin):
    """Абстрактная модель BaseItem для содержимого курса"""
    
    owner = models.ForeignKey(
        User,
        related_name='%(class)s_related',
        on_delete=models.CASCADE,
        verbose_name='Владелец',
    )
    
    title = models.CharField(
        max_length=500,
        verbose_name='Название',
    )
    
    class Meta:
        abstract = True
