from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from courses.models import Course, Subject
from courses.api.serializers import CourseSerializer, SubjectSerializer


class SubjectListView(generics.ListAPIView):
    """APi-эндпоинт для списка предметов"""
    
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """API-эндпоинт получения детальной информации о предмете"""
    
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для модели Course"""
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseEnrollView(APIView):
    """API-эндпоинт зачисления студента на курс"""
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({
            'enrolled': True,
        })
