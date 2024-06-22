from django.shortcuts import render
from django.http import JsonResponse
from .models import Profesor
from blog.models import Post

# Create your views here.
    
def membri(request):

    profesori = Profesor.objects.all()
    profesori = list(profesori)
    profesori.sort(key = lambda profesor : (profesor.nume, profesor.prenume)) # sortam dupa nume si prenume

    anunturi = Post.objects.all()
    anunturi = list(anunturi)
    if len(anunturi) > 4:
        anunturi = anunturi[:4]

    

    context = {
        "profesori" : profesori,
        "anunturi" : anunturi
    }

    return render(request, 'membri.html', context)

def prezentare(request):

    anunturi = Post.objects.all()
    anunturi = list(anunturi)
    if len(anunturi) > 4:
        anunturi = anunturi[:4]

    context = {
        "anunturi" : anunturi
    }

    return render(request, 'prezentare.html', context)

def organizare(request):
    profesori = Profesor.objects.all()
    profesori = list(profesori)
    profesori.sort(key = lambda profesor : (profesor.nume, profesor.prenume)) # sortam dupa nume si prenume

    anunturi = Post.objects.all()
    anunturi = list(anunturi)
    if len(anunturi) > 4:
        anunturi = anunturi[:4]

    context = {
        "profesori" : profesori,
        "anunturi" : anunturi
    }

    return render(request, 'organizare.html', context)