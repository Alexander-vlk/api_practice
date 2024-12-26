from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveBigIntegerField):
    """Поле порядка следования элементов курса"""
    
    def __init__(self, for_fields=None, *args, **kwargs):
        """Расширение метода __init__"""
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)
        
    def pre_save(self, model_instance, add):
        """Расширение метода pre_save"""
        if getattr(model_instance, self.attname):
            return super().pre_save(model_instance, add)
        
        queryset = self.model.objects.all()
        try:
            if self.for_fields:
                query_dict = {field: getattr(model_instance, field) for field in self.for_fields}
                queryset = queryset.filter(**query_dict)
                
            last_item = queryset.latest(self.attname)
            value = last_item.order + 1
        except ObjectDoesNotExist:
            value = 0
            
        setattr(model_instance, self.attname, value)
        
        return value

        