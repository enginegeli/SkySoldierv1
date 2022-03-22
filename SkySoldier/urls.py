from unicodedata import name
from django.urls import path, include
from SkySoldier.views import yazi



urlpatterns = [
    path('',yazi,name="yazi"),
]