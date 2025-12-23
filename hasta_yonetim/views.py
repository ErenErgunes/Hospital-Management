# hasta_yonetim/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Doktor, GelenMesaj, RandevuTalebi, HastaYorumu
from .forms import IletisimForm, RandevuTalepForm, HastaYorumuForm

def ana_sayfa(request):
    return render(request, 'anasayfa.html')

def doktorlari_listele(request):
    doktorlar = Doktor.objects.all()
    return render(request, 'doktorlar.html', {'doktorlar': doktorlar})

def bolumleri_goster(request):
    return render(request, 'bolumlerimiz.html')
    

def iletisim_sayfasi(request):
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            yeni_mesaj = GelenMesaj(
                ad_soyad = form.cleaned_data['ad_soyad'],
                email = form.cleaned_data['email'],
                mesaj = form.cleaned_data['mesaj']
            )
            yeni_mesaj.save()

            context = {
                'form': IletisimForm(), 
                'success_message': 'Mesajınız başarıyla gönderildi. Teşekkür ederiz!'
            }
            return render(request, 'iletisim.html', context)
        else:
            context = {'form': form}
            return render(request, 'iletisim.html', context)
    else:
        form = IletisimForm()
        context = {'form': form}
        return render(request, 'iletisim.html', context)

def doktor_detay(request, doktor_id):
    doktor = get_object_or_404(Doktor, pk=doktor_id)
    return render(request, 'doktor_detay.html', {'doktor': doktor})

def randevu_al(request):
    if request.method == 'POST':
        form = RandevuTalepForm(request.POST)
        if form.is_valid():
            form.save() 
            
            context = {
                'form': RandevuTalepForm(),
                'success_message': 'Randevu talebiniz başarıyla alınmıştır. Sizinle en kısa sürede iletişime geçeceğiz. Teşekkür ederiz!'
            }
            return render(request, 'randevu_al.html', context)
        else:
            context = {'form': form}
            return render(request, 'randevu_al.html', context)
    else:
        form = RandevuTalepForm()
        context = {'form': form}
        return render(request, 'randevu_al.html', context)

def hasta_yorumlari(request):
    yorumlar = HastaYorumu.objects.filter(yayinda=True).order_by('-olusturulma_tarihi')
    context = {
        'yorumlar': yorumlar
    }
    return render(request, 'yorumlar.html', context)

def yorum_ekle(request):
    if request.method == 'POST':
        form = HastaYorumuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hasta-yorumlari')
    else:
        form = HastaYorumuForm()
    
    return render(request, 'yorum_form.html', {'form': form, 'baslik': 'Siz de Görüşünüzü Paylaşın'})

def yorum_duzenle(request, id):
    yorum = get_object_or_404(HastaYorumu, id=id)
    
    if not request.user.is_staff:
        return redirect('hasta-yorumlari')

    if request.method == 'POST':
        form = HastaYorumuForm(request.POST, request.FILES, instance=yorum)
        if form.is_valid():
            form.save()
            return redirect('hasta-yorumlari')
    else:
        form = HastaYorumuForm(instance=yorum)

    return render(request, 'yorum_form.html', {'form': form, 'baslik': 'Yorumu Düzenle'})

def yorum_sil(request, yorum_id):
    yorum = get_object_or_404(HastaYorumu, id=yorum_id)
    if request.user.is_staff:
        yorum.delete()
    return redirect('hasta-yorumlari')