from django.shortcuts import render
from .models import Post
from django.utils.translation import activate

def articol(request, name):

    activate('ro')

    try:
        _anunt = Post.objects.get(titlu = name)
    except:
        return render(request, '404.html') # return 404 daca nu exista rezultat al acestui query. pentru rezultate multiple la fel, desi nu e cazul
                                           # campul titlu este unic.

    anunturi = Post.objects.all()
    anunturi = list(anunturi)
    if len(anunturi) > 4:
        anunturi = anunturi[:4]

    context = {
        "anunt" : _anunt,
        "anunturi" : anunturi
    }


    return render(request, 'blog/articol-detalii.html', context)
