from django import template


register = template.Library()

@register.filter
def model_name(obj):
    """Получение названия модели"""
    try:
        return obj._meta.model_name
    except AttributeError:
        return None
