from django.shortcuts import render
from programe_de_studii import models
from blog.models import Post

def specializari(request):

    _specializari = models.Specializare.objects.all()
    
    lista_specializari = [specializare for specializare in _specializari]

    anunturi = Post.objects.all()
    anunturi = list(anunturi)
    if len(anunturi) > 4:
        anunturi = anunturi[:4]

    context = {
        "specializari" : lista_specializari,
        "anunturi" : anunturi
    }

    return render(request, 'specializari/all.html', context)

def specializare(request, name):

    try:
        _specializare = models.Specializare.objects.get(nume = name)
    except:
        return render(request, '404.html') # return 404 daca nu exista rezultat al acestui query. pentru rezultate multiple la fel, desi nu e cazul
                                           # campul nume este unic.

    # aceste query-uri pot fi merge-uite insa trebuie gasita o alta solutie pentru returnarea unui 404 daca nu exista specializare
    # to be fixed!
    denumiri_specializari = models.Specializare.objects.all()
    denumiri_specializari = list(denumiri_specializari)
    denumiri_specializari = [spec.nume for spec in denumiri_specializari]

    coduri_cor = list(_specializare.coduri_cor.all())

    orare = models.Orar.objects.filter(specializare=_specializare.pk)
    orare = list(orare)
    orare.sort(key = lambda orar : (orar.an, orar.semestru))

    cursuri = models.Curs.objects.filter(specializare=_specializare.pk)
    cursuri = list(cursuri)
    cursuri.sort(key = lambda curs : (curs.an, curs.semestru))

    planuri = models.PlanDeInvatamant.objects.filter(specializare=_specializare.pk)
    planuri = list(planuri)
    planuri.sort(key = lambda plan : plan.an)

    anunturi = Post.objects.all()
    anunturi = list(anunturi)
    if len(anunturi) > 4:
        anunturi = anunturi[:4]

    context = {
        "specializare" : _specializare,
        "coduri_cor" : coduri_cor,
        "orare" : orare,
        "cursuri" : cursuri,
        "planuri" : planuri,
        "denumiri_specializari" : denumiri_specializari,
        "anunturi" : anunturi
    }

    return render(request, 'specializari/specializare.html', context)