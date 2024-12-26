from django.urls import reverse_lazy


from courses.models import Course
from utils.mixins.permissions import OwnerMixin, OwnerEditMixin


class OwnerCourseMixin(OwnerMixin):
    """Миксин для владельца курса"""
    
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    """Миксин для редактирования курса владельцем"""
    
    template_name = 'courses/manage/course/form.html'
