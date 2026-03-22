<?php
/**
 * Salva Film: titolo obbligatorio; anno e durata allineati allo schema (NULL consentiti).
 * mysqli bind_param con NULL su interi richiede PHP 8.1+.
 */
header('Content-Type: application/json; charset=utf-8');

require_once __DIR__ . '/db_config.php';

$codice = isset($_POST['Codice']) && $_POST['Codice'] !== '' ? (int) $_POST['Codice'] : null;
$titolo = isset($_POST['Titolo']) ? trim($_POST['Titolo']) : '';
$anno   = isset($_POST['Anno']) && $_POST['Anno'] !== '' ? (int) $_POST['Anno'] : null;
$durata = isset($_POST['Durata']) && $_POST['Durata'] !== '' ? (int) $_POST['Durata'] : null;
$lingua = isset($_POST['Lingua']) ? trim($_POST['Lingua']) : '';

if ($titolo === '') {
    echo json_encode([
        'success' => false,
        'message' => 'Il titolo è obbligatorio.',
    ]);
    exit;
}

if ($anno !== null && ($anno < 1900 || $anno > 2100)) {
    echo json_encode(['success' => false, 'message' => 'Anno non valido (usa 1900–2100 o lascia vuoto).']);
    exit;
}
if ($durata !== null && $durata < 1) {
    echo json_encode(['success' => false, 'message' => 'Durata deve essere almeno 1 minuto se indicata.']);
    exit;
}

if ($codice === null) {
    $stmt = $mysqli->prepare(
        'INSERT INTO Film (titolo, anno, durata, lingua) VALUES (?, ?, ?, ?)'
    );
    if (!$stmt) {
        echo json_encode(['success' => false, 'message' => 'Errore INSERT: ' . $mysqli->error]);
        exit;
    }
    $stmt->bind_param('siis', $titolo, $anno, $durata, $lingua);
    $ok = $stmt->execute();
    if ($ok) {
        echo json_encode([
            'success'  => true,
            'isUpdate' => false,
            'message'  => 'Film inserito correttamente (codice ' . $stmt->insert_id . ').',
        ]);
    } else {
        echo json_encode(['success' => false, 'message' => $stmt->error]);
    }
    $stmt->close();
} else {
    $stmt = $mysqli->prepare(
        'UPDATE Film SET titolo = ?, anno = ?, durata = ?, lingua = ? WHERE codice = ?'
    );
    if (!$stmt) {
        echo json_encode(['success' => false, 'message' => 'Errore UPDATE: ' . $mysqli->error]);
        exit;
    }
    $stmt->bind_param('siisi', $titolo, $anno, $durata, $lingua, $codice);
    $ok = $stmt->execute();
    if ($ok) {
        echo json_encode([
            'success'  => true,
            'isUpdate' => true,
            'message'  => 'Film aggiornato correttamente.',
        ]);
    } else {
        echo json_encode(['success' => false, 'message' => $stmt->error]);
    }
    $stmt->close();
}
