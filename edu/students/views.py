from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


class StudentRegisterView(CreateView):
    """View регистрации студентов"""
    
    template_name = 'stundents/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')
    
    def form_valid(self, form):
        data = form.cleaned_data
        
        user = authenticate(
            username=data['username'],
            password=data['password1'],
        )
        
        login(self.request, user)
        
        return super().form_valid(form)
    
    
