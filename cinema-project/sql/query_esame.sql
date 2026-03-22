-- Query principale (da esame): biglietti venduti per proiezione
SELECT
    p.numProiezione,
    f.titolo,
    p.sala,
    p.data,
    p.ora,
    COUNT(b.numPosto) AS bigliettiVenduti
FROM Proiezione p
JOIN Film f ON p.filmProiettato = f.codice
LEFT JOIN Biglietto b ON p.numProiezione = b.numProiezione
GROUP BY p.numProiezione, f.titolo, p.sala, p.data, p.ora
ORDER BY p.data, p.ora;
