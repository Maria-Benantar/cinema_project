# Cinema — Gestione Film

**Stack:** HTML5, CSS3, jQuery, AJAX, PHP, MySQL  
**Database:** `cinema` (tabelle Sala, Film, Proiezione, Biglietto)

## Struttura

```
cinema-project/
├── config.php · db_config.php
├── index.html · index.php
├── get_film.php · save_film.php · delete_film.php
├── css/style.css · js/script.js
├── sql/database.sql · sql/query_esame.sql
└── docs/relazione.txt
```

## Installazione (MAMP)

1. Copia la cartella in `htdocs/`.
2. Importa **`sql/database.sql`** in phpMyAdmin.
3. In **`config.php`**, se serve, imposta `DB_PASS` su `''` (password vuota in MAMP).

## URL (esempio)

`http://localhost:8888/cinema-project/index.php`

## CRUD

Tabella **`Film`**: `codice`, `titolo`, `anno`, `durata`, `lingua` (AJAX).  
`titolo` obbligatorio; `anno` e `durata` opzionali (NULL in DB). PHP **8.1+** consigliato.

**Query d’esame:** `sql/query_esame.sql`.

## Sviluppo (debug PHP opzionale)

Crea **`config.local.php`** nella stessa cartella di `config.php` con:

```php
<?php
$cinema_debug = true;
```

Oppure variabile d’ambiente `CINEMA_DEBUG=1`. **Non** includere `config.local.php` nella consegna se non richiesto.
