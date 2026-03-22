<?php
/**
 * Configurazione ambiente e credenziali database.
 *
 * SICUREZZA — debug disattivato di default
 * ----------------------------------------
 * Non mostrare mai errori PHP, stack trace o dettagli DB agli utenti finali.
 * Il valore predefinito di CINEMA_DEBUG è sempre FALSE nel codice versionato.
 * Per lo sviluppo locale abilita il debug solo tramite:
 *   • file opzionale `config.local.php` con `$cinema_debug = true;`, oppure
 *   • variabile d’ambiente `CINEMA_DEBUG=1`.
 * Non committare config.local.php; non impostare mai CINEMA_DEBUG=true nel repository.
 */

// Default sicuro: MAI true qui — solo false finché non viene sovrascritto da config.local.php o da env.
$cinema_debug = false;

if (is_file(__DIR__ . '/config.local.php')) {
    require __DIR__ . '/config.local.php';
}

if (!defined('CINEMA_DEBUG')) {
    $env = getenv('CINEMA_DEBUG');
    if ($env !== false && $env !== '') {
        $fromEnv = filter_var($env, FILTER_VALIDATE_BOOLEAN, FILTER_NULL_ON_FAILURE);
        define('CINEMA_DEBUG', $fromEnv === null ? false : (bool) $fromEnv);
    } else {
        define('CINEMA_DEBUG', (bool) $cinema_debug);
    }
}

if (CINEMA_DEBUG) {
    error_reporting(E_ALL);
    ini_set('display_errors', '1');
    ini_set('display_startup_errors', '1');
} else {
    error_reporting(E_ALL);
    ini_set('display_errors', '0');
    ini_set('display_startup_errors', '0');
    ini_set('log_errors', '1');
}

/** Credenziali MySQL (usate da db_config.php) */
if (!defined('DB_HOST')) {
    define('DB_HOST', 'localhost');
}
if (!defined('DB_USER')) {
    define('DB_USER', 'root');
}
if (!defined('DB_PASS')) {
    define('DB_PASS', 'root');
}
if (!defined('DB_NAME')) {
    define('DB_NAME', 'cinema');
}
