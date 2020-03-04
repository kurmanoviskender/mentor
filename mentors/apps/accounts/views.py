from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView
from django.views.generic.base import View


from .forms import StudentSignUpForm, TeacherSignUpForm
from .models import User, Teacher, Student, Comment


def index(request):
    return render(request, 'index.html')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/student_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('categories')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/teacher_signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        # cv = form.cleaned_data['CV']
        # self.object = form.save(cv=cv)
        # self.object.save()
        user = form.save()
        login(self.request, user)
        return redirect('categories')


class MyLoginView(LoginView):
    template_name = 'templates/accounts/login.html'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'accounts/teacher_detail.html'


class AddCommentView(CreateView):
    model = Comment
    template_name = 'accounts/add_comment.html'

    # fields = [
    #      'name', 'email', 'body',
    # ]
    fields = '__all__'


