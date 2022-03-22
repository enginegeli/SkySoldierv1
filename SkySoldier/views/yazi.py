from multiprocessing import context
from django.shortcuts import render , redirect
from SkySoldier.models import YazilarModel
from SkySoldier.forms import YaziFormu
from SkySoldier.models import YazilarModel
from algorithms.transformers import Transformers

def yazi(request):
    form =YaziFormu()
    if request.method == 'POST':
        form = YaziFormu(request.POST)
        if form.is_valid():
            yazi = YazilarModel()
            yazi.icerik = form.cleaned_data['metin']
            yazi.baslik = form.cleaned_data['baslik']
            yazi.yazar = request.user
            summi = Transformers()
            yazi.ozet = summi.summarize(str(form.cleaned_data['metin']))
            yazi.save()
            return redirect('yazi')
    
    yazilar = YazilarModel.objects.all()

    return render(request, 'pages/anasayfa.html',context={
        'form' : form,
        'yazilar' : yazilar
    })