from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.categories.models import Category


class User(AbstractUser):

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'student {self.user}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cv = models.TextField( default='CV')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'teacher {self.user}'


class Comment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

