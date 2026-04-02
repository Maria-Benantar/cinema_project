from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Proiezione
from sale.models import Sala
from film.models import Film
from biglietti.models import Biglietto
from datetime import datetime

def lista(request):
    proiezioni = Proiezione.objects.all()
    context = {'proiezioni': proiezioni}
    return render(request, 'proiezioni/lista.html', context)

def dettaglio(request, pk):
    proiezione = get_object_or_404(Proiezione, pk=pk)
    biglietti = proiezione.biglietti.all()
    context = {'proiezione': proiezione, 'biglietti': biglietti}
    return render(request, 'proiezioni/dettaglio.html', context)

def crea(request):
    if request.method == 'POST':
        sala_id = request.POST.get('sala')
        film_id = request.POST.get('film')
        data_ora = request.POST.get('data_ora')
        prezzo_biglietto = request.POST.get('prezzo_biglietto')
        
        sala = Sala.objects.get(pk=sala_id)
        film = Film.objects.get(pk=film_id)
        
        proiezione = Proiezione.objects.create(
            sala=sala,
            film=film,
            data_ora=data_ora,
            prezzo_biglietto=prezzo_biglietto,
            posti_disponibili=sala.numero_posti
        )
        
        # Create tickets for all seats
        for fila in range(1, sala.numero_file + 1):
            for posto in range(1, sala.posti_per_fila + 1):
                Biglietto.objects.create(
                    proiezione=proiezione,
                    numero_fila=chr(64 + fila),
                    numero_posto=posto,
                    prezzo=prezzo_biglietto
                )
        
        messages.success(request, f'Proiezione creata con successo!')
        return redirect('proiezioni_dettaglio', pk=proiezione.pk)
    
    sale = Sala.objects.all()
    film = Film.objects.all()
    context = {'sale': sale, 'film': film, 'action': 'Crea'}
    return render(request, 'proiezioni/form.html', context)

def modifica(request, pk):
    proiezione = get_object_or_404(Proiezione, pk=pk)
    
    if request.method == 'POST':
        proiezione.data_ora = request.POST.get('data_ora')
        proiezione.prezzo_biglietto = request.POST.get('prezzo_biglietto')
        proiezione.save()
        messages.success(request, f'Proiezione aggiornata con successo!')
        return redirect('proiezioni_dettaglio', pk=proiezione.pk)
    
    sale = Sala.objects.all()
    film = Film.objects.all()
    context = {'proiezione': proiezione, 'sale': sale, 'film': film, 'action': 'Modifica'}
    return render(request, 'proiezioni/form.html', context)

def elimina(request, pk):
    proiezione = get_object_or_404(Proiezione, pk=pk)
    proiezione.delete()
    messages.success(request, f'Proiezione eliminata con successo!')
    return redirect('proiezioni_lista')
