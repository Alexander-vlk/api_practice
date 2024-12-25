from django.contrib import admin

from courses.models import Course, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'updated_at', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'slug']
    
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Админ для Course"""
    list_display = ['id', 'title', 'owner', 'updated_at', 'created_at']
    list_display_links = ['title']
    raw_id_fields = ['owner', 'subject']
    search_fields = ['title', 'owner', 'overview']
