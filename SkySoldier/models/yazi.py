from enum import unique
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

class YazilarModel(models.Model):
    baslik = models.CharField(max_length=100)
    icerik = RichTextField()
    ozet = models.CharField(max_length=1000,default="")
    olusturulma_tarihi=models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = "baslik", unique=True )
    yazar = models.ForeignKey(User, related_name='yazilar',on_delete=models.CASCADE)

    class Meta:
        verbose_name="Yazi"
        verbose_name_plural="Yazilar"
        db_table="Yazi"

    def __str__(self):
        return self.baslik