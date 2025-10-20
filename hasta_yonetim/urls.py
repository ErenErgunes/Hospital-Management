# hasta_yonetim/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ana_sayfa, name='ana-sayfa'),
    path('doktorlar/', views.doktorlari_listele, name='doktorlar'),
    path('bolumlerimiz/', views.bolumleri_goster, name='bolumlerimiz'),
    path('iletisim/', views.iletisim_sayfasi, name='iletisim'),
    path('doktorlar/<int:doktor_id>/', views.doktor_detay, name='doktor-detay'),
    path('randevu-al/', views.randevu_al, name='randevu-al'),
]