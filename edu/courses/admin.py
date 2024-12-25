from django.contrib import admin

from courses.models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'updated_at', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'slug']
