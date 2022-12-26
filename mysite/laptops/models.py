from django.db import models
from django.db.models import CharField

class Todo(models.Model):
    task = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)

class person(models.Model):
        id = models.CharField(db_column = 'Id',primary_key=True,max_length = 4)
        Marka = models.CharField(db_column = 'Marka',max_length=30)
        Model = models.CharField(db_column = 'Model',max_length=100)
        Isletim_Sistemi = models.CharField(db_column = 'Isletim Sistemi',max_length=100)
        Islemci = models.CharField(db_column = 'Islemci',max_length=100)
        Bellek = models.CharField(db_column = 'Bellek',max_length=30)
        Disk = models.CharField(db_column = 'Disk',max_length=50)
        Ekran_Boyutu = models.CharField(db_column = 'Ekran Boyutu',max_length=20)
        Puan = models.CharField(db_column = 'Puan',max_length=3)
        Fiyat = models.CharField(db_column = 'Fiyat',max_length=7)
        Baslik = models.CharField(db_column = 'Baslik',max_length=255)
        Resim = models.CharField(db_column = 'Foto',max_length=255)
        Site = models.CharField(db_column = 'Site',max_length=12)
        Link = models.CharField(db_column = 'Link',max_length=200)


        def save(self,*args, **kwargs):
            super().save(*args, **kwargs)
    
        def __str__(self):
            return self.id + "--" + self.Baslik

        class Meta:
            managed = False
            db_table = 'person'

class ortak(models.Model):
        id = models.CharField(db_column = 'Id',primary_key=True,max_length = 4)
        Marka = models.CharField(db_column = 'Marka',max_length=30)
        Model = models.CharField(db_column = 'Model',max_length=100)
        Isletim_Sistemi = models.CharField(db_column = 'Isletim Sistemi',max_length=100)
        Islemci = models.CharField(db_column = 'Islemci',max_length=100)
        Bellek = models.CharField(db_column = 'Bellek',max_length=30)
        Disk = models.CharField(db_column = 'Disk',max_length=50)
        Ekran_Boyutu = models.CharField(db_column = 'Ekran Boyutu',max_length=20)
        Baslik = models.CharField(db_column = 'Baslik',max_length=255)
        Resim = models.CharField(db_column = 'Foto',max_length=255)
        N11 = models.CharField(db_column = 'N11',max_length=50)
        Hepsi = models.CharField(db_column = 'Hepsiburada',max_length=50)
        Trend = models.CharField(db_column = 'Trendyol',max_length=50)


        def save(self,*args, **kwargs):
            super().save(*args, **kwargs)
    
        def __str__(self):
            return self.id + "--" + self.Baslik

        class Meta:
            managed = False
            db_table = 'ortak'            

