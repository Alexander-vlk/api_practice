from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from utils.fields import OrderField
from utils.mixins.auto_date import AutoDateMixin
from utils.mixins.base_item import BaseItem


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


class Course(AutoDateMixin):
    """Модель курсов"""
    
    owner = models.ForeignKey(
        User,
        related_name='courses',
        on_delete=models.CASCADE,
        verbose_name='Владелец',
    )
    
    subject = models.ForeignKey(
        Subject,
        related_name='courses',
        on_delete=models.CASCADE,
        verbose_name='Предмет',
    )
    
    title = models.CharField(
        max_length=500,
        verbose_name='Название',
    )
    slug = models.SlugField(
        max_length=500,
        unique=True,
    )
    
    overview = models.CharField(
        max_length=2000,
        verbose_name='Описание',
    )
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-updated_at']
        
    def __str__(self):
        return self.title


class Module(AutoDateMixin):
    """Модель для модуля курса"""
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
    )
    
    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )
    
    overview = models.CharField(
        max_length=500,
        verbose_name='Описание',
    )
    
    text = models.CharField(
        max_length=5000,
        blank=True,
        verbose_name='Текстовое содержимое',
    )
    
    order = OrderField(
        blank=True,
        for_fields=['course'],
        verbose_name='Порядок модуля',
    )
    
    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['order']
        
    def __str__(self):
        return f'{self.order}: {self.title}'


class Content(AutoDateMixin):
    """Модель контента"""
    
    module = models.ForeignKey(
        Module,
        related_name='contents',
        on_delete=models.CASCADE,
        verbose_name='Модуль',
    )
    
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': [
            'text',
            'video',
            'image',
            'file',
        ]},
        verbose_name='Тип контента',
    )
    
    object_id = models.PositiveIntegerField(
        verbose_name='ID объекта',
    )
    
    order = OrderField(
        blank=True,
        default=0,
        for_fields=['module'],
        verbose_name='Порядок элемента',
    )
    
    item = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контенты'
        ordering = ['order']


class Text(BaseItem):
    """Модель Text для контента"""
    
    content = models.CharField(
        max_length=5000,
        verbose_name='Текст',
    )
    
    
class File(BaseItem):
    """Модель File для контента"""

    file = models.FileField(
        upload_to=settings.MEDIA_ROOT / 'files',
        verbose_name='Файл',
    )
    
    
class Image(BaseItem):
    """Модель Image для контента"""
    
    image = models.ImageField(
        upload_to=settings.MEDIA_ROOT / 'course_images',
        verbose_name='Изображение',
    )
    
    
class Video(BaseItem):
    """Модель Video для контента"""
    
    url = models.URLField(
        verbose_name='URL',
    )
