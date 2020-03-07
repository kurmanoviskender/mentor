from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView
from django.views.generic.base import View

from .forms import StudentSignUpForm, TeacherSignUpForm, CommentForm
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


class TeacherDetailView(FormView, DetailView):
    model = Teacher
    template_name = 'accounts/teacher_detail.html'
    form_class = CommentForm
    def form_valid(self, form):
        form = form.save(commit= False)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        form.teacher = Teacher.objects.get(pk=self.kwargs['pk'])
        print(form.teacher)
        form.author = self.request.user
        print(form.author)
        form.save()
        return super(TeacherDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('teacher_detail', kwargs={'pk':self.kwargs['pk']})








