# hasta_yonetim/views.py DOSYASININ OLMASI GEREKEN DOĞRU HALİ

# 1. Bütün import'lar dosyanın en üstünde toplanır.
from django.shortcuts import render
from .models import Doktor

# 2. ana_sayfa fonksiyonu sadece bir kere tanımlanır.
def ana_sayfa(request):
    return render(request, 'anasayfa.html')

# 3. doktorlari_listele fonksiyonu, doktorlar sayfasını gönderir ve biter.
def doktorlari_listele(request):
    # Veritabanındaki BÜTÜN Doktor nesnelerini çekiyoruz.
    doktorlar = Doktor.objects.all()
    
    # doktorlar listesini 'doktorlar.html' şablonuna gönderiyoruz.
    # Bir fonksiyon sadece bir kez return yapabilir.
    return render(request, 'doktorlar.html', {'doktorlar': doktorlar})
