from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.categories.models import Category
from django.urls import reverse


class User(AbstractUser):

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'student {self.user}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='teacher_user')
    cv = models.TextField(default='CV')
    category = models.ManyToManyField(Category, related_name='teacher_category')

    def __str__(self):
        return f'teacher {self.user}'

    def get_absolute_url(self):
        return reverse('teacher_detail', args=[self.id])


class Comment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_comments', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)

