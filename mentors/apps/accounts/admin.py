from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.forms import StudentSignUpForm, TeacherSignUpForm
from apps.accounts.models import User, Teacher, Student


# class CustomUserAdmin(UserAdmin):
#     add_form = StudentSignUpForm
#     # form = TeacherSignUpForm
#     model = User
#     list_display = ('username', 'email', 'is_staff', 'is_student', 'is_teacher')
#     class Meta:
#         fields = ('username', 'email', 'is_student', 'is_teacher')

# class CustomTeacherAdmin(UserAdmin):
#     add_form = TeacherSignUpForm
#     # form = CustomUserChangeForm
#     model = User
#     list_display = ('username', 'email', 'is_staff', 'is_student', 'is_teacher')

admin.site.register(User)