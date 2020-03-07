from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Student, Teacher, User, Comment
from ..categories.models import Category


class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    CV = forms.CharField(widget=forms.Textarea)
    avatar = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
            print(self.cleaned_data)
            teacher = Teacher.objects.create(user=user)
            teacher.category.add(*self.cleaned_data.get('category'))
            teacher.cv = self.cleaned_data.get('CV')
            teacher.avatar = self.cleaned_data.get('avatar')
            teacher.save()
        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
