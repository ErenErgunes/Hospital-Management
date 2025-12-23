from django.db import models

class Doktor(models.Model):
    isim_soyisim = models.CharField(max_length=100)
    uzmanlik_alani = models.CharField(max_length=100)
    biyografi = models.TextField()
    fotograf = models.ImageField(upload_to='doktorlar/', null=True, blank=True)

    def __str__(self):
        return self.isim_soyisim

class GelenMesaj(models.Model):
    ad_soyad = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad_soyad} ({self.email}) - {self.olusturulma_tarihi.strftime('%d-%m-%Y %H:%M')}"

class RandevuTalebi(models.Model):
    ad_soyad = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefon = models.CharField(max_length=20)
    
    # İLİŞKİSEL ALAN (ForeignKey):
    # Bu alan, Doktor modelimizle bir ilişki kurar.
    # Bir doktor silinirse (models.CASCADE), ilgili randevu talebi de silinir.
    doktor = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    
    # TARİH ALANI:
    # Bu, Django'ya bunun bir tarih olduğunu söyler.
    istedigi_tarih = models.DateField()
    
    # Ek notlar için
    mesaj = models.TextField(blank=True, null=True) 
    
    # Talep tarihi
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad_soyad} - {self.doktor.isim_soyisim} için ({self.istedigi_tarih})"
class HastaYorumu(models.Model):
    ad_soyad = models.CharField(max_length=100)
    PUAN_SECENEKLERI = [
        (1, '★☆☆☆☆ (1 Yıldız)'),
        (2, '★★☆☆☆ (2 Yıldız)'),
        (3, '★★★☆☆ (3 Yıldız)'),
        (4, '★★★★☆ (4 Yıldız)'),
        (5, '★★★★★ (5 Yıldız)'),
    ]
    puan = models.IntegerField(choices=PUAN_SECENEKLERI, default=5)
    yorum = models.TextField()
    
    dosya = models.FileField(upload_to='yorum_dosyalari/', blank=True, null=True)
    
    yayinda = models.BooleanField(default=True) 
    
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad_soyad} - {self.puan} Yıldız"