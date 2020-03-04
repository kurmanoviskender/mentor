from django.urls import path, include
from .views import CategoriesListView, filter_by_cat, AllTeachersView
from apps.accounts.models import Teacher



urlpatterns =[
    path('', CategoriesListView.as_view(), name ='categories'),
    path('<int:pk>/', filter_by_cat, name ='filter_teachers'),
    path('all_teachers', AllTeachersView.as_view(), name='all_teachers'),



]