from django.contrib import admin
from SkySoldier.models import YazilarModel
# Register your models here.



@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_field= (
        'baslik', 'icerik'
    )
    list_display = (
        'baslik' , 'olusturulma_tarihi' , 'duzenlenme_tarihi'
    )


