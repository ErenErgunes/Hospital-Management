# hastane_projesi/hastane_projesi/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # YENİ IMPORT
from django.conf.urls.static import static  # YENİ IMPORT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hasta_yonetim.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)