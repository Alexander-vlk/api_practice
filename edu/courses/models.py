from django.db import models
from django.contrib.auth.models import User

from utils.mixins.auto_date import AutoDateMixin


class Subject(AutoDateMixin):
    """Модель предмета, по которому идут курсы"""
    
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Слаг',
    )
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        
    def __str__(self):
        return self.title
