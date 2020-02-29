from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView
from django.views.generic.base import View

from .forms import StudentSignUpForm, TeacherSignUpForm
from .models import User, Teacher, Student


def index(request):
    return render(request, 'index.html')


class SignUpView(CreateView):
    model = User
    template_name = 'accounts/signup.html'
    fields= [

    ]


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
        user = form.save()
        login(self.request, user)
        return redirect('categories')


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'accounts/teacher_detail.html'