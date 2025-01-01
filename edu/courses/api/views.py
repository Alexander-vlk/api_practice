from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from courses.models import Course, Subject
from courses.api.serializers import SubjectSerializer


class SubjectListView(generics.ListAPIView):
    """APi-эндпоинт для списка предметов"""
    
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """API-эндпоинт получения детальной информации о предмете"""
    
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseEnrollView(APIView):
    """API-эндпоинт зачисления студента на курс"""
    
    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({
            'enrolled': True,
        })
