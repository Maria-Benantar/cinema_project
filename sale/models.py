from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    numero_posti = models.IntegerField()
    numero_file = models.IntegerField(default=10)
    posti_per_fila = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Sala'
        verbose_name_plural = 'Sale'

    def __str__(self):
        return f"{self.nome} ({self.numero_posti} posti)"
