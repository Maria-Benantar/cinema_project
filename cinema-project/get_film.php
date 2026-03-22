<?php
header('Content-Type: application/json; charset=utf-8');

require_once __DIR__ . '/db_config.php';

$data = [];
$success = true;
$message = '';

$sql = 'SELECT codice AS Codice, titolo AS Titolo, anno AS Anno, durata AS Durata, lingua AS Lingua
        FROM Film
        ORDER BY codice DESC';

if ($result = $mysqli->query($sql)) {
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    $result->free();
} else {
    $success = false;
    $message = 'Errore nella query: ' . $mysqli->error;
}

echo json_encode([
    'success' => $success,
    'message' => $message,
    'data'    => $data,
]);
