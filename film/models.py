from django.db import models

class Film(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True)
    regista = models.CharField(max_length=100)
    genere = models.CharField(max_length=50)
    durata_minuti = models.IntegerField()
    anno_uscita = models.IntegerField()
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['titolo']
        verbose_name = 'Film'
        verbose_name_plural = 'Film'

    def __str__(self):
        return f"{self.titolo} ({self.anno_uscita})"
