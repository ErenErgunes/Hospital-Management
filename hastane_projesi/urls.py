# hastane_projesi/hastane_projesi/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # İsteği 'hasta_yonetim' uygulamasına yönlendiriyor. DOĞRU!
    path('', include('hasta_yonetim.urls')), 
]