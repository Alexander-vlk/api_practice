from django.urls import path

from students import views

urlpatterns = [
    path('register/', views.StudentRegisterView.as_view(), name='register'),
    path('enroll/course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
]
