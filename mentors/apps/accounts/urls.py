from django.urls import include, path

from .views import StudentSignUpView, TeacherSignUpView, TeacherDetailView, MyLoginView,  AddCommentView

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(),  name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),   # переписал в auth.views!!
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name ='teacher_detail'),
    path('teacher/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

]