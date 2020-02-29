from django.urls import path, include
from .views import CategoriesListView, filter_by_cat
from apps.accounts.models import Teacher


urlpatterns =[
    path('', CategoriesListView.as_view(), name ='categories'),
    path('<int:pk>/', filter_by_cat, name ='filter_teachers')



]