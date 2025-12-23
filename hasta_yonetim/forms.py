# hasta_yonetim/forms.py

from django import forms
from .models import RandevuTalebi, HastaYorumu

class IletisimForm(forms.Form):
    ad_soyad = forms.CharField(label="Adınız Soyadınız", max_length=100)
    email = forms.EmailField(label="E-posta Adresiniz")
    mesaj = forms.CharField(label="Mesajınız", widget=forms.Textarea)

class RandevuTalepForm(forms.ModelForm):
    
    # TARİH ALANI İÇİN ÖZEL BİR DOKUNUŞ:
    # Django'ya bu alan için HTML5'in tarih seçme aracını (takvim) 
    # kullanmasını söylüyoruz.
    istedigi_tarih = forms.DateField(
        label="İstediğiniz Randevu Tarihi",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = RandevuTalebi  # Hangi modelden form oluşturulacak?
        
        # Modeldeki hangi alanlar formda gösterilsin?
        fields = ['ad_soyad', 'email', 'telefon', 'doktor', 'istedigi_tarih', 'mesaj']
        
        # Alanların etiketlerini (görünen isimlerini) güzelleştirelim
        labels = {
            'ad_soyad': 'Adınız Soyadınız',
            'email': 'E-posta Adresiniz',
            'telefon': 'Telefon Numaranız',
            'doktor': 'Doktor Seçiniz',
            'mesaj': 'Ek Notlarınız (Opsiyonel)',

        }
class HastaYorumuForm(forms.ModelForm):
    class Meta:
        model = HastaYorumu
        # 'dosya' alanını listeye ekledik
        fields = ['ad_soyad', 'puan', 'yorum', 'dosya'] 
        labels = {
            'ad_soyad': 'Adınız Soyadınız',
            'puan': 'Memnuniyet Puanınız',
            'yorum': 'Görüşleriniz',
            'dosya': 'Varsa Dosya/Fotoğraf Ekleyin (İsteğe bağlı)',
        }
        widgets = {
            'yorum': forms.Textarea(attrs={'rows': 4}),
        }