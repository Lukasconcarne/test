# Architektur

## Zweck

`test` ist das Benchmark-/Testbed-Repository der automatischen Aufgaben-Pipeline
(autodev). Es enthaelt eigenstaendige, kleine Python-Aufgabenmodule, die jeweils
ueber eine mitgelieferte pytest-Testdatei als ausfuehrbare Spezifikation
verfuegen, sowie eine statische HTML-Status-Seite. Es gibt kein
Gesamtprogramm und keinen gemeinsamen Laufzeit-Einstiegspunkt; die Module sind
voneinander unabhaengig.

## Tech-Stack

- Python 3 (>= 3.9, wegen Builtin-Generics wie `list[list[int]]` in den
  Signaturen), nur Standardbibliothek zur Laufzeit
- pytest als Testframework (Parametrisierung via `pytest.mark.parametrize`)
- Statisches HTML mit eingebettetem CSS, kein JavaScript, kein Build-Schritt

## Aufbau

Flache Struktur, alle Python-Dateien liegen im Repo-Root:

```
index.html              statische Status-Seite (deutsch, eingebettetes CSS)
roman_numerals.py       Aufgabenmodul: roemische Zahlen
merge_intervals.py      Aufgabenmodul: Intervalle zusammenfassen
group_sum.py            Aufgabenmodul: gruppieren und summieren
test_roman_numerals.py  pytest-Spezifikation zu roman_numerals
test_merge_intervals.py pytest-Spezifikation zu merge_intervals
test_group_sum.py       pytest-Spezifikation zu group_sum
```

## Module und Schnittstellen

Jedes Aufgabenmodul besteht aus oeffentlichen Funktionen, deren Verhalten im
Docstring der Funktion und in der zugehoerigen Testdatei festgelegt ist. Die
Testdatei ist die verbindliche Spezifikation; Implementierungen gehoeren
ausschliesslich in die jeweilige Moduldatei.

### `roman_numerals.py`

- `to_roman(n: int) -> str` – Ganzzahl 1..3999 in roemische Ziffern
  (Grossbuchstaben, subtraktive Schreibweise). `ValueError` bei `n < 1`,
  `n > 3999` oder keiner Ganzzahl.
- `from_roman(s: str) -> int` – kanonische roemische Zahl in Ganzzahl.
  `ValueError` bei ungueltiger oder nicht-kanonischer Eingabe
  (z.B. `""`, `"IIII"`, `"VV"`, `"IL"`).
- Vertrag: `from_roman(to_roman(n)) == n` fuer alle `n` in 1..3999
  (Roundtrip-Test).

### `merge_intervals.py`

- `merge(intervals: list[list[int]]) -> list[list[int]]` – fasst ueberlappende
  **oder sich beruehrende** Intervalle `[start, end]` zusammen
  (`[1,3]` + `[3,5]` -> `[1,5]`), Ergebnis nach `start` aufsteigend sortiert.
  Eingabe darf unsortiert sein; leere Eingabe -> `[]`; verschachtelte
  Intervalle werden vom umfassenden Intervall absorbiert.
  Die Eingabeliste wird nicht veraendert.

### `group_sum.py`

- `group_sum(rows: list[dict], key: str, value: str) -> list[tuple]` –
  gruppiert `rows` nach `rows[i][key]`, summiert `rows[i][value]` je Gruppe
  und liefert eine nach `key` aufsteigend sortierte Liste von
  `(key, summe)`-Tupeln. Leere Eingabe -> `[]`. Fehlt in einer Zeile `key`
  oder `value`, wird `KeyError` geworfen. Summen koennen int oder float sein.

## Datenfluesse und Zusammenspiel

- Testfluss pro Modul: `test_<modul>.py` importiert `<modul>` und ruft die
  oeffentlichen Funktionen direkt auf (reine Funktionen, kein I/O, keine
  Seiteneffekte, keine globalen Zustaende). Ausfuehrung: `pytest` im
  Repo-Root.
- `index.html` ist vollstaendig eigenstaendig (kein Bezug zu den
  Python-Modulen) und kann direkt im Browser geoeffnet oder statisch
  ausgeliefert werden.
- Es gibt keine projekteigenen Importe zwischen den Aufgabenmodulen.

## Konventionen

- Sprache: Code, Docstrings und UI-Texte auf Deutsch; in `.py`-Dateien
  ASCII-Umschreibungen statt Umlaute (`ue`, `oe`, `ss`).
- Type Hints in allen oeffentlichen Signaturen (Builtin-Generics,
  z.B. `list[list[int]]`).
- Fehlerbehandlung ueber Standard-Exceptions: `ValueError` fuer ungueltige
  Werte, `KeyError` fuer fehlende Schluessel.
- Reine Funktionen: Eingaben werden nicht mutiert, keine Abhaengigkeiten
  ausser Standardbibliothek (Laufzeit) bzw. pytest (Tests).
- Testdateien heissen `test_<modul>.py` und liegen neben dem Modul im Root.
