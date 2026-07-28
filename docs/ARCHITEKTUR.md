# Architektur

## Zweck
Dieses Repo ("test") ist die Teststrecke der automatischen Aufgaben-Pipeline
(autodev-Generalprobe). Es enthält kleine, voneinander unabhängige
Python-Aufgabenmodule. Jedes Modul wird als Stub mit Docstring-Vertrag und
`raise NotImplementedError` angelegt; die dazugehörigen pytest-Tests sind die
ausführbare Spezifikation, gegen die implementiert wird. Ergänzend liegt eine
eigenständige statische Status-Seite bei.

## Tech-Stack
- Python 3, ausschließlich Standardbibliothek (keine Runtime-Abhängigkeiten)
- pytest als Testframework (Tests nutzen u. a. `pytest.mark.parametrize`
  und `pytest.raises`)
- Statisches HTML mit eingebettetem CSS (kein Build-Schritt, kein Server)

## Struktur
Flache Ablage im Repo-Root – ein Modul pro Aufgabe nach festem Muster:

| Datei | Inhalt |
|---|---|
| `<modul>.py` | Aufgabenmodul: Stub bzw. Implementierung, Docstring = Vertrag |
| `test_<modul>.py` | pytest-Tests = ausführbare Spezifikation |
| `index.html` | eigenständige statische Status-Seite (ohne Bezug zu den Modulen) |
| `README.md` | Projekt-Kurzbeschreibung |

Die Module importieren nichts voneinander; es gibt keine Paketebene und
keine Shared-Utils.

## Module und Schnittstellen

### roman_numerals.py
- `to_roman(n: int) -> str` – Ganzzahl 1..3999 in römische Ziffern
  (Großbuchstaben, kanonische Subtraktivnotation). `ValueError` bei
  n < 1, n > 3999 oder keiner Ganzzahl.
- `from_roman(s: str) -> int` – kanonische römische Zahl zurück in eine
  Ganzzahl. `ValueError` bei ungültiger oder nicht-kanonischer Eingabe
  (z. B. `IIII`, `VV`, `IL`, leerer String).
- Spezifikation: `test_roman_numerals.py` (inkl. Roundtrip über 1..3999).

### merge_intervals.py
- `merge(intervals: list[list[int]]) -> list[list[int]]` – fasst
  überlappende ODER sich berührende Intervalle `[start, end]` zusammen
  (`[1,3]` + `[3,5]` -> `[1,5]`). Ergebnis nach Start aufsteigend sortiert,
  Eingabe darf unsortiert sein, leere Eingabe -> `[]`. Die Eingabeliste
  bleibt unverändert (kein In-Place).
- Spezifikation: `test_merge_intervals.py`.

### group_sum.py
- `group_sum(rows: list[dict], key: str, value: str) -> list[tuple]` –
  gruppiert `rows` nach `rows[i][key]`, summiert `rows[i][value]` je Gruppe
  und liefert eine nach `key` aufsteigend sortierte Liste von
  `(key, summe)`-Tupeln. Leere Eingabe -> `[]`; fehlt in einer Zeile `key`
  oder `value`, wird `KeyError` geworfen.
- Spezifikation: `test_group_sum.py`.

## Datenfluss
Es gibt keine Laufzeit-Anwendung und keinen Datenfluss zwischen den Modulen.
Der Fluss ist pro Aufgabe immer derselbe:

```
Aufgabe (Stub + test_<modul>.py) -> Implementierung in <modul>.py -> pytest
```

Die Tests importieren ihr Modul direkt (`from <modul> import ...`) und prüfen
die im Docstring zugesagten Verträge inklusive Fehlerfälle. `index.html` ist
statisch und an keinen Datenfluss angeschlossen.

## Schnittstellen-Konventionen
- Reine Funktionen mit Typannotationen; Rückgabe neuer Objekte statt Mutation
  der Eingaben.
- Fehlerfälle über die im Docstring genannten Standard-Ausnahmen
  (`ValueError`, `KeyError`) – keine eigenen Exception-Typen.
- Docstrings und Fehlertexte auf Deutsch.
