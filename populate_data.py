import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_project.settings')
django.setup()

from sale.models import Sala
from film.models import Film
from proiezioni.models import Proiezione
from biglietti.models import Biglietto

# Clear existing data
Biglietto.objects.all().delete()
Proiezione.objects.all().delete()
Sala.objects.all().delete()
Film.objects.all().delete()

# Create Rooms
sala1 = Sala.objects.create(nome="Sala 1 - Premium", numero_posti=100, numero_file=10, posti_per_fila=10)
sala2 = Sala.objects.create(nome="Sala 2 - Standard", numero_posti=80, numero_file=8, posti_per_fila=10)
sala3 = Sala.objects.create(nome="Sala 3 - Piccola", numero_posti=50, numero_file=5, posti_per_fila=10)

# Create Films
film1 = Film.objects.create(
    titolo="Dune: Part Two",
    descrizione="L'epica continua mentre Paul Atreides si addentra nel deserto di Arrakis.",
    regista="Denis Villeneuve",
    genere="Fantascienza",
    durata_minuti=166,
    anno_uscita=2024,
    rating=8.5
)

film2 = Film.objects.create(
    titolo="Oppenheimer",
    descrizione="La storia del fisico J. Robert Oppenheimer e il Progetto Manhattan.",
    regista="Christopher Nolan",
    genere="Dramma",
    durata_minuti=180,
    anno_uscita=2023,
    rating=8.3
)

film3 = Film.objects.create(
    titolo="Barbie",
    descrizione="Barbie scopre il mondo reale e affronta una nuova avventura.",
    regista="Greta Gerwig",
    genere="Commedia",
    durata_minuti=114,
    anno_uscita=2023,
    rating=7.9
)

film4 = Film.objects.create(
    titolo="Killers of the Flower Moon",
    descrizione="Un'indagine sui crimini contro la tribù Osage negli anni '20.",
    regista="Martin Scorsese",
    genere="Dramma",
    durata_minuti=206,
    anno_uscita=2023,
    rating=8.1
)

film5 = Film.objects.create(
    titolo="The Brutalist",
    descrizione="Un architetto ungherese cerca il successo in America.",
    regista="Brady Corbet",
    genere="Dramma",
    durata_minuti=215,
    anno_uscita=2023,
    rating=7.8
)

# Create Projections with Tickets
now = datetime.now()
projections_data = [
    (sala1, film1, now + timedelta(days=1, hours=19), 12.50),
    (sala1, film1, now + timedelta(days=2, hours=21), 12.50),
    (sala2, film2, now + timedelta(days=1, hours=17), 10.00),
    (sala2, film3, now + timedelta(days=2, hours=19), 9.50),
    (sala3, film4, now + timedelta(days=1, hours=20), 11.00),
    (sala3, film5, now + timedelta(days=3, hours=18), 11.00),
]

for sala, film, data_ora, prezzo in projections_data:
    proiezione = Proiezione.objects.create(
        sala=sala,
        film=film,
        data_ora=data_ora,
        prezzo_biglietto=prezzo,
        posti_disponibili=sala.numero_posti
    )
    
    # Create tickets for all seats
    for fila in range(1, sala.numero_file + 1):
        for posto in range(1, sala.posti_per_fila + 1):
            Biglietto.objects.create(
                proiezione=proiezione,
                numero_fila=chr(64 + fila),
                numero_posto=posto,
                prezzo=prezzo
            )

print("✓ Database populated successfully!")
print(f"  - {Sala.objects.count()} rooms created")
print(f"  - {Film.objects.count()} films created")
print(f"  - {Proiezione.objects.count()} projections created")
print(f"  - {Biglietto.objects.count()} tickets created")
