# hasta_yonetim/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ana_sayfa, name='ana-sayfa'),
    path('doktorlar/', views.doktorlari_listele, name='doktorlar'),
]