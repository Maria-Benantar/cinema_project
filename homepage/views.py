from django.shortcuts import render
from sale.models import Sala
from film.models import Film
from proiezioni.models import Proiezione
from biglietti.models import Biglietto

def index(request):
    context = {
        'num_sale': Sala.objects.count(),
        'num_film': Film.objects.count(),
        'num_proiezioni': Proiezione.objects.count(),
        'num_biglietti': Biglietto.objects.count(),
    }
    return render(request, 'homepage/index.html', context)
