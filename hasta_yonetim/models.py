from django.db import models

class Doktor(models.Model):
    isim_soyisim = models.CharField(max_length=100)
    uzmanlik_alani = models.CharField(max_length=100)
    biyografi = models.TextField()

    def __str__(self):
        return self.isim_soyisim