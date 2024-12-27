from django.urls import reverse_lazy
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from courses.forms import ModuleFormSet
from courses.models import Course
from courses.mixins import OwnerCourseMixin, OwnerCourseEditMixin


class ManageCourseListView(OwnerCourseMixin, ListView):
    """View для списка курсов пользователя"""
    
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/manage/course/list.html'
    permission_required = 'courses.view_course'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_course'


class CourseModuleTemplateView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/formset.html'
    course = None
    
    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)
    
    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner=request.user)
        return super().dispatch(request, pk)
    
    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({
            'course': self.course,
            'formset': formset,
        })
