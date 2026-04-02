from django.db import models
from proiezioni.models import Proiezione

class Biglietto(models.Model):
    SEAT_STATUS = [
        ('available', 'Disponibile'),
        ('reserved', 'Prenotato'),
        ('sold', 'Venduto'),
    ]
    
    proiezione = models.ForeignKey(Proiezione, on_delete=models.CASCADE, related_name='biglietti')
    numero_fila = models.CharField(max_length=2)
    numero_posto = models.IntegerField()
    stato = models.CharField(max_length=10, choices=SEAT_STATUS, default='available')
    prezzo = models.DecimalField(max_digits=6, decimal_places=2)
    data_vendita = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['numero_fila', 'numero_posto']
        verbose_name = 'Biglietto'
        verbose_name_plural = 'Biglietti'
        unique_together = ['proiezione', 'numero_fila', 'numero_posto']

    def __str__(self):
        return f"Biglietto {self.numero_fila}{self.numero_posto} - {self.proiezione}"
