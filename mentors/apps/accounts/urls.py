from django.urls import include, path

from .views import SignUpView, StudentSignUpView, TeacherSignUpView, TeacherDetailView

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name ='teacher_detail'),


]