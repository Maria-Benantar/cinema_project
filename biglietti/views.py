from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Biglietto
from proiezioni.models import Proiezione

def lista(request):
    biglietti = Biglietto.objects.all()
    proiezione_id = request.GET.get('proiezione')
    stato = request.GET.get('stato')
    
    if proiezione_id:
        biglietti = biglietti.filter(proiezione_id=proiezione_id)
    if stato:
        biglietti = biglietti.filter(stato=stato)
    
    proiezioni = Proiezione.objects.all()
    context = {
        'biglietti': biglietti,
        'proiezioni': proiezioni,
        'proiezione_selezionata': proiezione_id,
        'stato_selezionato': stato,
    }
    return render(request, 'biglietti/lista.html', context)

def dettaglio(request, pk):
    biglietto = get_object_or_404(Biglietto, pk=pk)
    context = {'biglietto': biglietto}
    return render(request, 'biglietti/dettaglio.html', context)

def vendi(request, pk):
    biglietto = get_object_or_404(Biglietto, pk=pk)
    
    if biglietto.stato == 'available':
        biglietto.stato = 'sold'
        biglietto.data_vendita = timezone.now()
        biglietto.save()
        
        # Update projection available seats
        proiezione = biglietto.proiezione
        proiezione.posti_disponibili = proiezione.biglietti.filter(stato='available').count()
        proiezione.save()
        
        messages.success(request, f'Biglietto venduto con successo!')
    else:
        messages.error(request, f'Questo biglietto non è disponibile.')
    
    return redirect('biglietti_dettaglio', pk=pk)

def libera(request, pk):
    biglietto = get_object_or_404(Biglietto, pk=pk)
    
    if biglietto.stato in ['reserved', 'sold']:
        biglietto.stato = 'available'
        biglietto.data_vendita = None
        biglietto.save()
        
        # Update projection available seats
        proiezione = biglietto.proiezione
        proiezione.posti_disponibili = proiezione.biglietti.filter(stato='available').count()
        proiezione.save()
        
        messages.success(request, f'Biglietto liberato con successo!')
    else:
        messages.error(request, f'Questo biglietto è già disponibile.')
    
    return redirect('biglietti_dettaglio', pk=pk)
