<?php
header('Content-Type: application/json; charset=utf-8');

require_once __DIR__ . '/db_config.php';

$codice = isset($_POST['Codice']) ? (int) $_POST['Codice'] : 0;

if ($codice <= 0) {
    echo json_encode(['success' => false, 'message' => 'Codice film non valido.']);
    exit;
}

$stmt = $mysqli->prepare('DELETE FROM Film WHERE codice = ?');
if (!$stmt) {
    echo json_encode(['success' => false, 'message' => 'Errore DELETE: ' . $mysqli->error]);
    exit;
}

$stmt->bind_param('i', $codice);
$ok = $stmt->execute();

if ($ok && $stmt->affected_rows > 0) {
    echo json_encode(['success' => true, 'message' => 'Film eliminato (eventuali proiezioni e biglietti collegati sono stati rimossi).']);
} else {
    echo json_encode([
        'success' => false,
        'message' => 'Nessun film con questo codice oppure errore nell\'eliminazione.',
    ]);
}

$stmt->close();
