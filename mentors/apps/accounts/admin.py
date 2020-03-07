from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.forms import StudentSignUpForm, TeacherSignUpForm
from apps.accounts.models import User, Teacher, Student, Comment


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
admin.site.register(Teacher)
admin.site.register(Student)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'teacher', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)