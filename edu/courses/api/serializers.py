from rest_framework import serializers

from courses.models import Course, Content, Module, Subject


class SubjectSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Subject"""
    
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']
        

class ModuleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Module"""
    
    class Meta:
        model = Module
        fields = ['order', 'title', 'overview']


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Course"""
   
    modules = ModuleSerializer(many=True, read_only=True)
   
    class Meta:
        model = Course
        fields = [
            'id',
            'subject',
            'title',
            'slug',
            'overview',
            'created_at',
            'updated_at',
            'owner',
            'modules',
        ]


class ItemRelatedField(serializers.RelatedField):
    """Поле-сериализатор"""
    
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Content"""
    
    item = ItemRelatedField(read_only=True)
    
    class Meta:
        model = Content
        fields = ['order', 'item']
