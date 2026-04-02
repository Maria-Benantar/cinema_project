from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Film

def lista(request):
    film = Film.objects.all()
    genere = request.GET.get('genere')
    anno = request.GET.get('anno')
    
    if genere:
        film = film.filter(genere__icontains=genere)
    if anno:
        film = film.filter(anno_uscita=anno)
    
    generi = Film.objects.values_list('genere', flat=True).distinct()
    anni = Film.objects.values_list('anno_uscita', flat=True).distinct().order_by('-anno_uscita')
    
    context = {
        'film': film,
        'generi': generi,
        'anni': anni,
        'genere_selezionato': genere,
        'anno_selezionato': anno,
    }
    return render(request, 'film/lista.html', context)

def dettaglio(request, pk):
    f = get_object_or_404(Film, pk=pk)
    context = {'film': f}
    return render(request, 'film/dettaglio.html', context)

def crea(request):
    if request.method == 'POST':
        titolo = request.POST.get('titolo')
        descrizione = request.POST.get('descrizione')
        regista = request.POST.get('regista')
        genere = request.POST.get('genere')
        durata_minuti = request.POST.get('durata_minuti')
        anno_uscita = request.POST.get('anno_uscita')
        rating = request.POST.get('rating', 0.0)
        
        film = Film.objects.create(
            titolo=titolo,
            descrizione=descrizione,
            regista=regista,
            genere=genere,
            durata_minuti=durata_minuti,
            anno_uscita=anno_uscita,
            rating=rating
        )
        messages.success(request, f'Film {titolo} creato con successo!')
        return redirect('film_dettaglio', pk=film.pk)
    
    return render(request, 'film/form.html', {'action': 'Crea'})

def modifica(request, pk):
    film = get_object_or_404(Film, pk=pk)
    
    if request.method == 'POST':
        film.titolo = request.POST.get('titolo')
        film.descrizione = request.POST.get('descrizione')
        film.regista = request.POST.get('regista')
        film.genere = request.POST.get('genere')
        film.durata_minuti = request.POST.get('durata_minuti')
        film.anno_uscita = request.POST.get('anno_uscita')
        film.rating = request.POST.get('rating')
        film.save()
        messages.success(request, f'Film {film.titolo} aggiornato con successo!')
        return redirect('film_dettaglio', pk=film.pk)
    
    context = {'film': film, 'action': 'Modifica'}
    return render(request, 'film/form.html', context)

def elimina(request, pk):
    film = get_object_or_404(Film, pk=pk)
    titolo = film.titolo
    film.delete()
    messages.success(request, f'Film {titolo} eliminato con successo!')
    return redirect('film_lista')
