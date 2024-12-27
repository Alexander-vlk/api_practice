from django.apps import apps
from django.forms.models import modelform_factory
from django.urls import reverse_lazy
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView

from courses.forms import ModuleFormSet
from courses.models import Content, Course, Module
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
    """View для создания курса"""
    
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    """View для обновления курса"""
    
    permission_required = 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    """View для удаления курса"""
    
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_course'


class CourseModuleTemplateView(TemplateResponseMixin, View):
    """View для набора форм модулей к курсу"""
    
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
        
    def post(self, request, *args, **kwargs):
        formsset = self.get_formset(data=request.POST)
        if formsset.is_valid():
            formsset.save()
            return redirect('manage_course_list')
        
        return self.render_to_response({
            'course': self.course,
            'formset': self.formset,
        })


class ContentCreateUpdateView(TemplateResponseMixin, View):
    """View для контента"""
    
    module = None
    model = None
    obj = None
    
    MODEL_NAMES = ['text', 'video', 'image', 'file']
    
    template_name = 'courses/manage/content/form.html'
    
    def get_model(self, model_name):
        if not model_name in self.MODEL_NAMES:
            return None
        
        return apps.get_model(app_label='courses', model_name=model_name)
    
    def get_form(self, model, *args, **kwargs):
        form = modelform_factory(
            model,
            exclude=[
                'owner',
                'order',
                'created_at',
                'updated_at',
            ]
        )
        return form(*args, **kwargs)
    
    def dispatch(self, request, module_id,  model_name, id=None):
        self.module = get_object_or_404(
            Module,
            id=module_id,
            course__owner=request.user,
        )
        self.model = self.get_model(model_name)
        
        if id:
            self.obj = get_object_or_404(
                self.model,
                id=id,
                owner=request.user,
            )
        
        return super().dispatch(request, module_id, model_name, id)
    
    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, isinstance=self.obj)
        return self.render_to_response({
            'form': form,
            'object': self.obj,
        })
        
    def post(self, request, module_id, model_name, id=None):
        form = self.get_form(
            self.model,
            isinstance=self.obj,
            data=request.POST,
            files=request.FILES,
        )
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            
            if not id:
                Content.objects.create(
                    module=self.module,
                    item=obj,
                )
            
            return redirect('module_content_list', self.module.id)
    
        return self.render_to_response({
            'form': form,
            'object': self.obj,
        })


class ContentDeleteView(View):
    """View удаления контента"""
    
    def post(self, request, id):
        content = get_object_or_404(
            Content,
            id=id,
            module__course__owner=request.user,
        )
        module = content.module
        content.item.delete()
        content.delete()
        return redirect('module_content_list', module.id)
