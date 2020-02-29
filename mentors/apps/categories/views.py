from django.shortcuts import render

from .models import Category
from apps.accounts.models import Teacher
from django.views.generic import View, ListView, DetailView


class CategoriesListView(ListView):
    model = Category
    template_name = 'categories/categories.html'

# class FilterTeachersView(ListView):
#     model = Teacher
#     template_name = 'categories/filter_teachers.html'

def filter_by_cat(request, pk):
    filtered_cat = Category.objects.get(pk=pk)
    filtered_teacher = Teacher.objects.filter(category=filtered_cat)
    return render(request, 'categories/filter_teachers.html', {'filtered_teacher': filtered_teacher})





