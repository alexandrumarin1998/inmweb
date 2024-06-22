from django.shortcuts import render
from programe_de_studii.models import Specializare
from .models import Examen, Document
import json
import datetime
from blog.models import Post

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

def examene(request):

    ani = []
    data_curenta = datetime.datetime.now()
    septembrie = 9

    an_curent = data_curenta.year if data_curenta.month >= septembrie else data_curenta.year - 1
    for i in range(an_curent - 2020 + 1):
        an_1 = 2020 + i
        an_2 = an_1 + 1
        ani.append((i, f"{an_1} - {an_2}"))

    specializari = Specializare.objects.all()
    specializari = list(specializari)
    specializari = [specializare.acronim for specializare in specializari]

    examene = Examen.objects.all()
    documente = Document.objects.all()
    documente = list(documente)

    licente = len([examen for examen in examene if examen.specializare.ciclu == "Licenta"])
    disertatii = len(examene) - licente

    anunturi = Post.objects.all()
    anunturi = list(anunturi)
    if len(anunturi) > 4:
        anunturi = anunturi[:4]

    context = {
        "years" : ani,
        "specializari" : specializari,
        "examene" : examene,
        "documente" : documente,
        "licente" : licente,
        "disertatii" : disertatii,
        "anunturi" : anunturi
    }

    return render(request, "examene.html", context)

@csrf_exempt
def examene_continut(request):
    query = json.loads(request.body)

    nume = query["name"] # la nume e stupid ca trebuie perfect match.
    tokens = query["checks"]

    tokens_ani = [int(token) for token in tokens if token.isdigit()]
    tokens_specializari = [token for token in tokens if not token.isdigit()]

    examene = Examen.objects.all()

    if len(tokens_ani):
        examene = examene.filter(anul__in=tokens_ani)

    if len(tokens_specializari):
        examene = examene.filter(specializare__acronim__in=tokens_specializari)

    if len(tokens_ani) and len(tokens_specializari):
        examene = examene.filter(anul__in=tokens_ani).filter(specializare__acronim__in=tokens_specializari)

    examene = list(examene)

    if len(nume):
        studenti_examene = [examen.student for examen in examene]
        potriviri = [student for student in studenti_examene if nume.lower() in student.lower()]
        examene = [examen for examen in examene if examen.student in potriviri]

    documente = Document.objects.all()
    documente = list(documente)

    anunturi = Post.objects.all()
    anunturi = list(anunturi)
    if len(anunturi) > 4:
        anunturi = anunturi[:4]

    context = {
        "examene" : examene,
        "documente" : documente,
        "anunturi" : anunturi
    }

    return render(request, "examene_continut.html", context)