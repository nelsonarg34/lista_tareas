from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from rest_framework import routers


urlpatterns = [
    # Admin routes
    path('admin/', admin.site.urls),

    # Api routes
    path('users/', include('authentication.urls')),
    path('api/',include('list.routers')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
