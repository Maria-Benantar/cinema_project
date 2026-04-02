from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Sala

def lista(request):
    sale = Sala.objects.all()
    context = {'sale': sale}
    return render(request, 'sale/lista.html', context)

def dettaglio(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    context = {'sala': sala}
    return render(request, 'sale/dettaglio.html', context)

def crea(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        numero_posti = request.POST.get('numero_posti')
        numero_file = request.POST.get('numero_file', 10)
        posti_per_fila = request.POST.get('posti_per_fila', 10)
        
        sala = Sala.objects.create(
            nome=nome,
            numero_posti=numero_posti,
            numero_file=numero_file,
            posti_per_fila=posti_per_fila
        )
        messages.success(request, f'Sala {nome} creata con successo!')
        return redirect('sale_dettaglio', pk=sala.pk)
    
    return render(request, 'sale/form.html', {'action': 'Crea'})

def modifica(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    
    if request.method == 'POST':
        sala.nome = request.POST.get('nome')
        sala.numero_posti = request.POST.get('numero_posti')
        sala.numero_file = request.POST.get('numero_file')
        sala.posti_per_fila = request.POST.get('posti_per_fila')
        sala.save()
        messages.success(request, f'Sala {sala.nome} aggiornata con successo!')
        return redirect('sale_dettaglio', pk=sala.pk)
    
    context = {'sala': sala, 'action': 'Modifica'}
    return render(request, 'sale/form.html', context)

def elimina(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    nome = sala.nome
    sala.delete()
    messages.success(request, f'Sala {nome} eliminata con successo!')
    return redirect('sale_lista')
