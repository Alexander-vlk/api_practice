from rest_framework import serializers

from courses.models import Course, Module, Subject


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
