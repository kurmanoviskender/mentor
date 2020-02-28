from django.shortcuts import render

from .models import Category
from django.views.generic import View, ListView, DetailView


class CategoriesListView(ListView):
    model = Category
    template_name = 'categories/categories.html'





