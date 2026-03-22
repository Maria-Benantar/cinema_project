-- ============================================
-- CREAZIONE DATABASE
-- ============================================
CREATE DATABASE IF NOT EXISTS cinema
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE cinema;

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Biglietto;
DROP TABLE IF EXISTS Proiezione;
DROP TABLE IF EXISTS Film;
DROP TABLE IF EXISTS Sala;
SET FOREIGN_KEY_CHECKS = 1;

-- =========================
-- TABELLA SALA
-- =========================
CREATE TABLE Sala (
    numero INT PRIMARY KEY,
    numPosti INT NOT NULL,
    dim INT,
    numFile INT,
    numPostiPerFila INT,
    tipo ENUM('3D', 'tradizionale') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =========================
-- TABELLA FILM
-- =========================
CREATE TABLE Film (
    codice INT AUTO_INCREMENT PRIMARY KEY,
    titolo VARCHAR(100) NOT NULL,
    anno INT NULL,
    durata INT NULL,
    lingua VARCHAR(50) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =========================
-- TABELLA PROIEZIONE
-- (ON DELETE CASCADE: eliminando un film si eliminano le proiezioni collegate)
-- =========================
CREATE TABLE Proiezione (
    numProiezione INT AUTO_INCREMENT PRIMARY KEY,
    sala INT,
    filmProiettato INT,
    data DATE,
    ora TIME,
    FOREIGN KEY (sala) REFERENCES Sala(numero),
    FOREIGN KEY (filmProiettato) REFERENCES Film(codice) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =========================
-- TABELLA BIGLIETTO
-- =========================
CREATE TABLE Biglietto (
    numProiezione INT,
    numFila INT,
    numPosto INT,
    dataVendita DATE,
    prezzo DECIMAL(5,2),
    PRIMARY KEY (numProiezione, numFila, numPosto),
    FOREIGN KEY (numProiezione) REFERENCES Proiezione(numProiezione) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =========================
-- DATI DI ESEMPIO
-- =========================

INSERT INTO Sala VALUES
(1, 200, 50, 10, 20, '3D'),
(2, 150, 40, 10, 15, 'tradizionale'),
(3, 120, 35, 8, 15, 'tradizionale'),
(4, 250, 60, 10, 25, '3D');

INSERT INTO Film (titolo, anno, durata, lingua) VALUES
('Dune', 2024, 166, 'EN'),
('Oppenheimer', 2023, 180, 'EN'),
('Interstellar', 2014, 169, 'EN'),
('Joker', 2019, 122, 'EN'),
('Inception', 2010, 148, 'EN');

INSERT INTO Proiezione (sala, filmProiettato, data, ora) VALUES
(1, 1, '2025-03-20', '18:00:00'),
(1, 2, '2025-03-20', '21:00:00'),
(2, 3, '2025-03-21', '20:00:00'),
(3, 4, '2025-03-22', '19:30:00'),
(4, 5, '2025-03-22', '22:00:00');

INSERT INTO Biglietto VALUES
(1, 1, 1, '2025-03-15', 8.50),
(1, 1, 2, '2025-03-15', 8.50),
(1, 2, 1, '2025-03-16', 8.50),
(2, 1, 1, '2025-03-16', 9.00),
(3, 3, 5, '2025-03-17', 7.50),
(3, 3, 6, '2025-03-17', 7.50),
(4, 1, 3, '2025-03-18', 8.00),
(5, 2, 4, '2025-03-18', 10.00);
