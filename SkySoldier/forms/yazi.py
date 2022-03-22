from django import forms

class YaziFormu(forms.Form):
    
    metin = forms.CharField(widget=forms.Textarea)
    baslik = forms.CharField()
    ozet = forms.CharField()