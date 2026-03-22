/**
 * Cinema — AJAX: get_film.php, save_film.php, delete_film.php
 * Tabella Film: codice, titolo, anno, durata, lingua
 */
$(function () {
    function showMsg($el, ok, title, text) {
        $el.removeClass('hidden message-success message-error');
        $el.addClass('message ' + (ok ? 'message-success' : 'message-error'));
        $el.html(
            '<span class="label">' + title.toUpperCase() + '</span><span>' + text + '</span>'
        );
    }

    function hideMsg($el) {
        $el.addClass('hidden').removeClass('message message-success message-error').empty();
    }

    function resetForm() {
        $('#film-form')[0].reset();
        $('#Codice').val('');
        $('#form-title').text('Creazione / Aggiornamento');
        $('#form-subtitle').html('Nuovo record nella tabella <code>Film</code>');
        $('#btn-annulla-modifica').hide();
        hideMsg($('#message-form'));
    }

    function setEdit(f) {
        $('#Codice').val(f.Codice);
        $('#Titolo').val(f.Titolo);
        // DB può avere NULL: input vuoti; niente required HTML su Anno/Durata
        $('#Anno').val(f.Anno != null && f.Anno !== '' ? f.Anno : '');
        $('#Durata').val(f.Durata != null && f.Durata !== '' ? f.Durata : '');
        $('#Lingua').val(f.Lingua || '');
        $('#form-title').text('Modifica film #' + f.Codice);
        $('#form-subtitle').text('Aggiorna i campi e salva (tabella Film).');
        $('#btn-annulla-modifica').show();
        hideMsg($('#message-form'));
    }

    function esc(s) {
        if (s == null) return '';
        return String(s)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    function loadFilms() {
        $.getJSON('get_film.php')
            .done(function (res) {
                var $tb = $('#film-table-body');
                $tb.empty();

                if (!res.success) {
                    showMsg($('#message-global'), false, 'Errore', res.message || 'Caricamento fallito.');
                    $('#film-count').text('0 film');
                    $('#empty-state').removeClass('hidden');
                    return;
                }

                hideMsg($('#message-global'));
                var list = res.data || [];
                $('#film-count').text(list.length + (list.length === 1 ? ' film' : ' film'));

                if (list.length === 0) {
                    $('#empty-state').removeClass('hidden');
                    return;
                }
                $('#empty-state').addClass('hidden');

                list.forEach(function (f) {
                    var anno = f.Anno != null && f.Anno !== '' ? f.Anno : '—';
                    var dur = f.Durata != null && f.Durata !== '' ? f.Durata : '—';
                    var ling = f.Lingua ? esc(f.Lingua) : '—';

                    $tb.append(
                        '<tr data-id="' + f.Codice + '">' +
                        '<td>' + f.Codice + '</td>' +
                        '<td>' + esc(f.Titolo) + '</td>' +
                        '<td>' + anno + '</td>' +
                        '<td>' + dur + '</td>' +
                        '<td><span class="badge">' + ling + '</span></td>' +
                        '<td class="actions-cell">' +
                        '<button type="button" class="btn-table edit">Modifica</button> ' +
                        '<button type="button" class="btn-table delete">Elimina</button>' +
                        '</td></tr>'
                    );
                });
            })
            .fail(function () {
                showMsg($('#message-global'), false, 'Errore', 'Impossibile contattare il server.');
                $('#film-count').text('0 film');
                $('#empty-state').removeClass('hidden');
            });
    }

    $('#film-form').on('submit', function (e) {
        e.preventDefault();
        hideMsg($('#message-form'));
        hideMsg($('#message-global'));

        $.ajax({
            url: 'save_film.php',
            method: 'POST',
            data: $(this).serialize(),
            dataType: 'json',
        })
            .done(function (res) {
                if (res.success) {
                    showMsg($('#message-form'), true, 'OK', res.message || 'Operazione riuscita.');
                    loadFilms();
                    if (!res.isUpdate) resetForm();
                } else {
                    showMsg($('#message-form'), false, 'Errore', res.message || 'Salvataggio fallito.');
                }
            })
            .fail(function () {
                showMsg($('#message-form'), false, 'Errore', 'Impossibile contattare il server.');
            });
    });

    $('#btn-nuovo-film, #btn-reset-form').on('click', resetForm);
    $('#btn-annulla-modifica').on('click', resetForm);

    $('#film-table-body').on('click', '.btn-table.edit', function () {
        var $tr = $(this).closest('tr');
        var id = $tr.data('id');
        var cells = $tr.children();
        setEdit({
            Codice: id,
            Titolo: cells.eq(1).text(),
            Anno: cells.eq(2).text() === '—' ? '' : cells.eq(2).text(),
            Durata: cells.eq(3).text() === '—' ? '' : cells.eq(3).text(),
            Lingua: cells.eq(4).text().trim() === '—' ? '' : cells.eq(4).text().trim(),
        });
        $('html, body').animate({ scrollTop: $('#film-form').offset().top - 40 }, 300);
    });

    $('#film-table-body').on('click', '.btn-table.delete', function () {
        var $tr = $(this).closest('tr');
        var id = $tr.data('id');
        var titolo = $tr.children().eq(1).text();
        if (!window.confirm('Eliminare il film "' + titolo + '" (codice ' + id + ')?\nVerranno rimosse anche le proiezioni e i biglietti collegati.')) return;

        $.ajax({
            url: 'delete_film.php',
            method: 'POST',
            data: { Codice: id },
            dataType: 'json',
        })
            .done(function (res) {
                if (res.success) {
                    showMsg($('#message-global'), true, 'OK', res.message || 'Eliminato.');
                    loadFilms();
                    if ($('#Codice').val() === String(id)) resetForm();
                } else {
                    showMsg($('#message-global'), false, 'Errore', res.message || 'Eliminazione fallita.');
                }
            })
            .fail(function () {
                showMsg($('#message-global'), false, 'Errore', 'Impossibile contattare il server.');
            });
    });

    loadFilms();
});
