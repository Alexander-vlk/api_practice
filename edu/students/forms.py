from django import forms 

from courses.models import Course


class CourseEnrollForm(forms.Form):
    """Форма зачисления студентов на курсы"""
    
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.HiddenInput
    )
