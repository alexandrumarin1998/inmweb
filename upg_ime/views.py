from typing import Any
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Link, Slider
from django.utils.translation import activate

def error_404(request, exception):
    return render(request, "404.html", {})

def index(request):
    activate('ro') # setat pentru anunturi sa apara luna abreviata in lb romana

    anunturi = Post.objects.all()
    if len(anunturi) > 6:
        anunturi = anunturi[:6]

    anunturi = list(anunturi)

    linkuri = Link.objects.all()
    linkuri = list(linkuri)

    link_button = [link for link in linkuri if link.plasament == 4]
    linkuri = [link for link in linkuri if link.plasament != 4]
    linkuri.sort(key = lambda link : link.plasament)

    slider = Slider.objects.all()
    slider = list(slider)

    context = {
        "anunturi" : anunturi,
        "linkuri" : linkuri,
        "link_button" : link_button,
        "slider" : slider
    }

    return render(request, 'index.html', context)
    
def contact(request):

    anunturi = Post.objects.all()
    anunturi = list(anunturi)
    if len(anunturi) > 4:
        anunturi = anunturi[:4]

    context = {
        "anunturi" : anunturi
    }

    return render(request, 'contact.html', context)

def burse(request):

    anunturi = Post.objects.all()
    anunturi = list(anunturi)
    if len(anunturi) > 4:
        anunturi = anunturi[:4]

    context = {
        "anunturi" : anunturi
    }

    return render(request, 'scholarship.html', context)