from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.categories.urls')),
    path('index/', index, name='index'),


    # path('signup/', include('apps.accounts.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

