from django.urls import path

from students import views

urlpatterns = [
    path('register/', views.StudentRegisterView.as_view(), name='register'),
    path('enroll/course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses', views.StudentCourseListView.as_view(), name='student_course_list'),
    path('course/<pk>/', views.StudentCourseDetailView.as_view(), name='student_course_detail'),
    
    path(
        'course/<pk>/<module_id>/', 
        views.StudentCourseDetailView.as_view(), 
        name='student_course_detail_module'
    ),
]
