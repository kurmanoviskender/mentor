from django.urls import path, include
from .views import CategoriesListView


urlpatterns =[
    path('', CategoriesListView.as_view(), name ='categories'),


]