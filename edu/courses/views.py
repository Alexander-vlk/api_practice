from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.views.generic.list import ListView

from courses.models import Course
from courses.mixins import OwnerCourseMixin, OwnerCourseEditMixin


class ManageCourseListView(ListView):
    """View для списка курсов пользователя"""
    
    model = Course
    template_name = 'courses/manage/course/list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    pass


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    pass


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
