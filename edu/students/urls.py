from django.urls import path

from students import views

urlpatterns = [
    path('register/', views.StudentRegisterView.as_view(), name='register'),
]
