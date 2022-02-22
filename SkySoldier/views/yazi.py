from multiprocessing import context
from django.shortcuts import render
from SkySoldier.models import YazilarModel
from SkySoldier.forms import YaziFormu


def yazi(request):
    form = YaziFormu()
    yazilar = YazilarModel.objects.all()

    return render(request, 'pages/anasayfa.html',context={
        'form' : form,
        'yazilar' : yazilar
    })