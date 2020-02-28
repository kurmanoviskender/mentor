from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.categories.urls')),
    # path('signup/', include('apps.accounts.urls')),

]
