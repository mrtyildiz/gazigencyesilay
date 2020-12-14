from django.db import models

class Etkinlik(models.Model):
    Etkinlik_adi = models.CharField(max_length=20, default='')
    Etkinlik_tanimi = models.CharField(max_length=20, default='')
    Etkinlik_link =  models.URLField(max_length=250)
    Etkinlik_img = models.ImageField(upload_to='Etkinlik')

    def __str__(self):
        return self.Etkinlik_adi

class Team(models.Model):
    Ad_Soyad = models.CharField(max_length=50, default='')
    Görevi = models.CharField(max_length=50, default='')
    Team_Foto = models.ImageField(upload_to='Team')
    Twitter_link =  models.URLField(max_length=250)
    linked_link =  models.URLField(max_length=250)
    def __str__(self):
        return self.Ad_Soyad


class Yessem(models.Model):
    Emded = models.CharField(max_length=50, default='')


    def __str__(self):
        return self.Emded