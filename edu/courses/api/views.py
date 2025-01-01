from rest_framework import generics

from courses.models import Subject
from courses.api.serializers import SubjectSerializer


class SubjectListView(generics.ListAPIView):
    """APi-эндпоинт для списка предметов"""
    
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """API-эндпоинт получения детальной информации о предмете"""
    
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
