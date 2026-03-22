<?php
require_once __DIR__ . '/config.php';
?>
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cinema — CRUD Film · Interfaccia 5</title>
    <link rel="stylesheet" href="css/style.css">
    <script src="https://code.jquery.com/jquery-3.7.1.min.js" crossorigin="anonymous"></script>
</head>
<body class="interfaccia-5 palette-bianca">
<div class="app-container interfaccia-5">
    <header class="ui-strip">
        <div class="ui-strip__titles">
            <h1>Gestione film</h1>
            <span class="subtitle">Tabella <strong>Film</strong> — operazioni <strong>Create, Read, Update, Delete</strong> tramite AJAX (senza ricaricare la pagina).</span>
        </div>
        <div class="ui-strip__meta">
            <span class="badge-ui" title="Specifica interfaccia e colori">Interfaccia <strong>5</strong> · Palette <strong>bianca</strong></span>
            <div class="header-actions">
                <button type="button" class="btn btn-ghost" id="btn-reset-form">Pulisci form</button>
                <button type="button" class="btn btn-primary" id="btn-nuovo-film">Nuovo film</button>
            </div>
        </div>
    </header>

    <div class="layout">
        <section class="card" aria-labelledby="section-elenco">
            <div class="card-header">
                <h2 id="section-elenco">Lettura · Elenco</h2>
                <span class="card-kicker" id="film-count">0 film</span>
            </div>
            <hr class="divider">
            <div id="message-global" class="hidden"></div>
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Codice</th>
                            <th>Titolo</th>
                            <th>Anno</th>
                            <th>Durata (min)</th>
                            <th>Lingua</th>
                            <th>Azioni</th>
                        </tr>
                    </thead>
                    <tbody id="film-table-body"></tbody>
                </table>
                <div id="empty-state" class="empty-state hidden">
                    Nessun film in archivio. Usa il pannello a destra per inserirne uno.
                </div>
            </div>
        </section>

        <section class="card" aria-labelledby="form-title">
            <div class="card-header">
                <h2 id="form-title">Creazione / Aggiornamento</h2>
                <span class="card-kicker" id="form-subtitle">Nuovo record nella tabella <code>Film</code></span>
            </div>
            <hr class="divider"/>

            <form id="film-form" autocomplete="off">
                <input type="hidden" name="Codice" id="Codice">

                <div class="form-grid">
                    <div class="form-group form-row-full">
                        <label for="Titolo">Titolo</label>
                        <input type="text" id="Titolo" name="Titolo" required maxlength="100" placeholder="Titolo del film">
                    </div>
                    <div class="form-group">
                        <label for="Anno">Anno <span class="hint-inline">(opzionale, come in DB)</span></label>
                        <input type="number" id="Anno" name="Anno" min="1900" max="2100" placeholder="es. 2024">
                    </div>
                    <div class="form-group">
                        <label for="Durata">Durata (min) <span class="hint-inline">(opzionale)</span></label>
                        <input type="number" id="Durata" name="Durata" min="1" placeholder="es. 120">
                    </div>
                    <div class="form-group form-row-full">
                        <label for="Lingua">Lingua</label>
                        <input type="text" id="Lingua" name="Lingua" maxlength="50" placeholder="es. EN, IT">
                    </div>
                </div>

                <div class="form-footer">
                    <div class="form-footer-left">
                        <div id="message-form" class="hidden"></div>
                    </div>
                    <div>
                        <button type="button" class="btn btn-ghost" id="btn-annulla-modifica" style="display:none;">Annulla modifica</button>
                        <button type="submit" class="btn btn-primary" id="btn-salva-film">Salva</button>
                    </div>
                </div>
            </form>
        </section>
    </div>
</div>

<script src="js/script.js"></script>
</body>
</html>
