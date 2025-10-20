# hasta_yonetim/views.py

from django.shortcuts import render, get_object_or_404 
from .models import Doktor, GelenMesaj, RandevuTalebi # RandevuTalebi modelini de ekleyelim
from .forms import IletisimForm, RandevuTalepForm # RandevuTalepForm'u buraya da import ediyoruz

# 1. ANA SAYFA FONKSİYONU (Hata büyük ihtimalle bu eksik)
def ana_sayfa(request):
    return render(request, 'anasayfa.html')

# 2. DOKTOR LİSTESİ FONKSİYONU
def doktorlari_listele(request):
    doktorlar = Doktor.objects.all()
    return render(request, 'doktorlar.html', {'doktorlar': doktorlar})

# 3. BÖLÜMLER FONKSİYONU
def bolumleri_goster(request):
    return render(request, 'bolumlerimiz.html')
    
# 4. İLETİŞİM FONKSİYONU (Bunu en son güncellemiştik)
# hasta_yonetim/views.py içindeki iletisim_sayfasi fonksiyonu

def iletisim_sayfasi(request):
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            # --- BURAYI GÜNCELLİYORUZ ---
            
            # Eski 'print' komutlarını siliyoruz.
            # Yerine, formdan gelen temiz verilerle yeni bir GelenMesaj nesnesi oluşturuyoruz
            yeni_mesaj = GelenMesaj(
                ad_soyad = form.cleaned_data['ad_soyad'],
                email = form.cleaned_data['email'],
                mesaj = form.cleaned_data['mesaj']
            )
            # ve bu nesneyi veritabanına kaydediyoruz!
            yeni_mesaj.save()

            # --- GÜNCELLEME BİTTİ ---
            
            # Kullanıcıya teşekkür mesajı göndermeye devam edelim
            context = {
                'form': IletisimForm(), 
                'success_message': 'Mesajınız başarıyla gönderildi. Teşekkür ederiz!'
            }
            return render(request, 'iletisim.html', context)
        else:
            # ... (form geçerli değilse kısmı aynı kalıyor) ...
            context = {'form': form}
            return render(request, 'iletisim.html', context)
    else:
        # ... (GET isteği kısmı aynı kalıyor) ...
        form = IletisimForm()
        context = {'form': form}
        return render(request, 'iletisim.html', context)

# 5. DOKTOR DETAY FONKSİYONU
def doktor_detay(request, doktor_id):
    doktor = get_object_or_404(Doktor, pk=doktor_id)
    return render(request, 'doktor_detay.html', {'doktor': doktor})

def randevu_al(request):
    if request.method == 'POST':
        # Kullanıcı formu göndermiş (POST isteği)
        form = RandevuTalepForm(request.POST)
        if form.is_valid():
            # Form geçerli. 
            # Bu bir ModelForm olduğu için, .save() demek yeterli!
            # Django, formdaki verileri alıp yeni bir RandevuTalebi 
            # nesnesi oluşturur ve veritabanına kaydeder. Çok havalı!
            form.save() 
            
            # Kullanıcıya bir teşekkür mesajı gönderelim
            context = {
                'form': RandevuTalepForm(), # Formu sıfırla, boş formu göster
                'success_message': 'Randevu talebiniz başarıyla alınmıştır. Sizinle en kısa sürede iletişime geçeceğiz. Teşekkür ederiz!'
            }
            return render(request, 'randevu_al.html', context)
        else:
            # Form geçerli değilse (örn: e-posta formatı yanlış)
            # dolu formu (hatalarla birlikte) tekrar sayfaya gönder.
            context = {'form': form}
            return render(request, 'randevu_al.html', context)
    else:
        # Kullanıcı sayfayı ilk kez ziyaret ediyor (GET isteği)
        form = RandevuTalepForm() # Boş bir form oluştur
        context = {'form': form}
        return render(request, 'randevu_al.html', context)