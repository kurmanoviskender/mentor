from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import index

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.categories.urls')),
    path('index/', index, name='index'),


    # path('signup/', include('apps.accounts.urls')),

]
