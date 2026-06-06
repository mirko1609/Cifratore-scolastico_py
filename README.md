# Cifrario di Cesare

Implementazione del Cifrario di Cesare in Python. Permette di cifrare e decifrare messaggi tramite sostituzione alfabetica con una chiave numerica, e include una modalità bruteforce per decriptare messaggi senza conoscere la chiave.

## Come funziona

Il Cifrario di Cesare è uno dei più antichi algoritmi crittografici: ogni lettera del messaggio viene sostituita con la lettera che si trova `n` posizioni più avanti nell'alfabeto, dove `n` è la chiave scelta.

**Esempio:** con chiave 3, la lettera `a` diventa `d`, la `b` diventa `e`, e così via.

## Modalità disponibili

- **`c` — Cifra** un messaggio con una chiave numerica a scelta
- **`d` — Decifra** un messaggio conoscendo la chiave
- **`b` — Bruteforce** prova tutte le 26 chiavi possibili e mostra tutti i risultati

## Esempio di output

```
=== Cifrario di Cesare ===

cosa vuoi fare? (c/d/b): c
inserisci la tua frase: ciao mondo
inserisci la tua chiave: 3
Frase cifrata: fldr prqgr

cosa vuoi fare? (c/d/b): b
inserisci la tua frase: fldr prqgr
=== BruteForce ===
chiave: 1, frase decifrata: ekcp oqpfq
chiave: 2, frase decifrata: djbo npoe p
chiave: 3, frase decifrata: ciao mondo
...
```

## Tecnologie

- Python 3

## Come eseguire

```bash
python cifratore-scolastico.py
```

## Note

Progetto scolastico realizzato durante il primo anno del triennio presso ITIS, indirizzo Informatica.
