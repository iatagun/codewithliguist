from django.db import models
import dizge


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Check(models.Model):
    phonetic = models.BooleanField("Fonetik Yaz (G2P)", default=False)
    harmony = models.BooleanField("Ünlü Uyumu", default=False)
    syllableH = models.BooleanField("Seslemlere Ayır", default=False)
    syllableM = models.BooleanField("Seslemlere Ayır (Dönüştürür)", default=False)
    syllableCount = models.BooleanField("Seslem Örüntülerini Say", default=False)
