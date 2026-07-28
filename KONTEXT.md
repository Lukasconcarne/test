# Kontext

## Ziel
Repo "test" ist die Generalprobe/Teststrecke der automatischen
Aufgaben-Pipeline. Es beherbergt kleine, unabhängige Python-Aufgaben, die
jeweils als Stub plus pytest-Spezifikation eingehen und von der Pipeline
implementiert werden. Das Repo soll dauerhaft ein sauberer, minimaler
Referenzaufbau bleiben.

## Konventionen
- Flache Struktur: genau EINE Datei pro Aufgabe (`<modul>.py`) plus Tests
  (`test_<modul>.py`) im Repo-Root; keine Pakete, keine Shared-Utils.
- Modul-Docstrings tragen die Vorgabe "Ändere NUR diese Datei" – die
  Bearbeitung einer Aufgabe beschränkt sich auf das jeweilige Modul.
- Tests sind die ausführbare Spezifikation; eine Implementierung gilt als
  korrekt, wenn `pytest test_<modul>.py` grün ist.
- Nur Python-Standardbibliothek zur Laufzeit; pytest ausschließlich als
  Test-Abhängigkeit.
- Schnittstellen: reine Funktionen mit Typannotationen, keine Mutation der
  Eingaben, Fehler über Standard-Exceptions (`ValueError`, `KeyError`).
- Sprache: Bezeichner auf Englisch, Docstrings/Doku/UI-Texte auf Deutsch.
- Module bleiben voneinander unabhängig – keine Cross-Imports zwischen
  Aufgabenmodulen.
- `index.html` ist eine eigenständige statische Seite ohne Build-Schritt;
  sie wird weder aus den Python-Modulen erzeugt noch von ihnen genutzt.

## Constraints
- Es gibt keine ausführbare Anwendung, keinen Server und keinen Build –
  nichts davon darf vorausgesetzt oder gestartet werden.
- Keine externen Runtime-Abhängigkeiten hinzufügen.
- Doku hält nur Dauerhaftes fest (Aufbau, Schnittstellen, Konventionen);
  Fortschritt und Status gehören ins Board, nicht in Dateien.

## Richtung
Neue Aufgaben folgen dem bestehenden Muster: Stub mit Docstring-Vertrag im
Root, dazu `test_<modul>.py` als Spezifikation. Die Architektur-Doku liegt in
`docs/ARCHITEKTUR.md` und wird bei neuen Modulen oder geänderten
Schnittstellen mitgepflegt.
