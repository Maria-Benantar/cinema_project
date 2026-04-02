from django.db import models
from sale.models import Sala
from film.models import Film

class Proiezione(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='proiezioni')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='proiezioni')
    data_ora = models.DateTimeField()
    prezzo_biglietto = models.DecimalField(max_digits=6, decimal_places=2)
    posti_disponibili = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['data_ora']
        verbose_name = 'Proiezione'
        verbose_name_plural = 'Proiezioni'

    def __str__(self):
        return f"{self.film.titolo} - {self.sala.nome} ({self.data_ora.strftime('%d/%m/%Y %H:%M')})"
