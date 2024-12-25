from django.contrib import admin

from courses.models import Course, Module, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """Админ для Subject"""
    
    list_display = ['id', 'title', 'slug', 'updated_at', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'slug']
    
    
class ModuleInline(admin.StackedInline):
    model = Module
    
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Админ для Course"""
    
    list_display = ['id', 'title', 'owner', 'updated_at', 'created_at']
    list_display_links = ['title']
    raw_id_fields = ['owner', 'subject']
    search_fields = ['title', 'owner', 'overview']
    prepopulated_fields = {"slug": ["title"]}
    inlines = [ModuleInline]
