# Architektur

## Zweck

`test` ist das Benchmark-Projekt der autodev-Pipeline: eine Sammlung kleiner,
voneinander unabhängiger Python-Aufgabenmodule, deren Vertrag vollständig
durch mitgelieferte pytest-Tests festgelegt ist, plus einer eigenständigen
statischen Status-Seite (`index.html`).

## Tech-Stack

- Python 3.9+ (die Signaturen nutzen eingebaute Generics wie
  `list[list[int]]`), ausschließlich Standardbibliothek
- pytest als Test-Runner (Tests = ausführbare Spezifikation)
- Statisches HTML mit eingebettetem CSS (`index.html`, kein Build-Schritt,
  kein JavaScript)

## Aufbau

Flache Struktur, keine Pakete:

```
<modul>.py          Aufgabenmodul (Implementierung)
test_<modul>.py     zugehörige pytest-Spezifikation
index.html          eigenständige Status-/Feature-Seite
README.md           Kurzbeschreibung
docs/ARCHITEKTUR.md diese Datei
KONTEXT.md          Projektkontext, Konventionen, Richtung
```

## Module

Alle Module sind unabhängig voneinander; es gibt keine Querimporte zwischen
ihnen.

### roman_numerals.py

- `to_roman(n: int) -> str` – Ganzzahl 1..3999 → römische Ziffern
  (Großbuchstaben, subtraktive Notation). `ValueError` bei n < 1, n > 3999
  oder keiner Ganzzahl.
- `from_roman(s: str) -> int` – kanonische römische Zahl → Ganzzahl.
  `ValueError` bei ungültiger oder nicht-kanonischer Eingabe
  (z. B. `IIII`, `VV`, `IL`, leerer String).
- Roundtrip-Garantie: `from_roman(to_roman(n)) == n` für alle n in 1..3999.

### merge_intervals.py

- `merge(intervals: list[list[int]]) -> list[list[int]]` – fasst überlappende
  ODER sich berührende Intervalle `[start, end]` zusammen
  (`[1,3]` und `[3,5]` → `[1,5]`). Eingabe darf unsortiert sein, Ergebnis ist
  nach start aufsteigend sortiert; leere Eingabe → `[]`.
  Die Eingabeliste wird nicht verändert.

### group_sum.py

- `group_sum(rows: list[dict], key: str, value: str) -> list[tuple]` –
  gruppiert `rows` nach `rows[i][key]`, summiert `rows[i][value]` je Gruppe
  und gibt eine nach key aufsteigend sortierte Liste von
  `(key, summe)`-Tupeln zurück. Leere Eingabe → `[]`; fehlt in einer Zeile
  `key` oder `value`, wird `KeyError` geworfen.

## Tests

- Genau eine Testdatei pro Modul (`test_<modul>.py`); sie importiert die
  Funktionen direkt (`from <modul> import ...`).
- Muster: einfache Testfunktionen mit Asserts, ergänzt um
  `pytest.mark.parametrize` für Wertetabellen und `pytest.raises` für
  Fehlerfälle.
- Ausführung: `pytest` (Repo-Root) oder gezielt `pytest test_<modul>.py`.

## Datenflüsse

Es gibt keinen Datenfluss zwischen den Modulen. Jedes Modul ist eine reine
Funktionseinheit: Eingabewerte → Rückgabewerte, ohne I/O, ohne globalen
Zustand, ohne Seiteneffekte (Eingaben werden nicht mutiert).

## Schnittstellen

Die öffentliche Schnittstelle eines Moduls sind genau die oben genannten
Funktionssignaturen. Der Vertrag (Verhalten, Fehlerfälle) steht im
Modul-Docstring und ist durch die Tests abgesichert. Fehler werden über
Ausnahmen signalisiert: `ValueError` für ungültige Werte, `KeyError` für
fehlende Dictionary-Schlüssel.

## index.html

Eigenständige, statische Status-/Feature-Seite ohne Abhängigkeit zu den
Python-Modulen; eingebettetes CSS, kein JavaScript, kein Backend.
