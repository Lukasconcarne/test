# Kontext

## Ziel

Dieses Repository ist das Testbed der automatischen Aufgaben-Pipeline
(autodev). Es dient als Uebungs- und Benchmark-Ziel, an dem die Pipeline
Aenderungen eigenstaendig vornehmen und gegen pytest-Spezifikationen pruefen
kann. Details zu Aufbau und Schnittstellen stehen in `docs/ARCHITEKTUR.md`.

## Konventionen

- **Sprache:** Dokumentation, Docstrings, Commit- und UI-Texte auf Deutsch.
  In Python-Quelldateien ASCII-Umschreibungen (`ue`, `oe`, `ss`) statt
  Umlaute verwenden.
- **Aufgabenmodule:** Ein Modul = eine Datei im Repo-Root mit wenigen
  oeffentlichen Funktionen. Die zugehoerige Testdatei `test_<modul>.py` ist
  die verbindliche Spezifikation und wird nicht an die Implementierung
  angepasst.
- **Stil:** Type Hints in Signaturen, reine Funktionen ohne Seiteneffekte,
  Eingabedaten nicht mutieren.
- **Fehler:** Standard-Exceptions (`ValueError`, `KeyError`) gemaess den in
  den Docstrings dokumentierten Vertraegen – keine eigenen
  Exception-Klassen.
- **Tests:** pytest, Ausfuehrung im Repo-Root; Parametrisierung ueber
  `pytest.mark.parametrize`, wo sinnvoll.

## Constraints

- Laufzeit-Code nutzt ausschliesslich die Python-Standardbibliothek;
  einzige externe Abhaengigkeit ist pytest (Tests).
- Keine Build- oder Deployment-Schritte; `index.html` ist statisch und
  eigenstaendig.
- Aenderungen an einem Aufgabenmodul duerfen dessen oeffentliche
  Schnittstelle (Namen, Signaturen, Fehlerverhalten) nicht brechen – die
  Testdateien definieren den Vertrag.

## Richtung

Das Repo waechst um weitere kleine, voneinander unabhaengige Aufgabenmodule
nach dem gleichen Muster: eine Moduldatei plus eine pytest-Testdatei als
ausfuehrbare Spezifikation. Module bleiben bewusst entkoppelt – keine
Querabhaengigkeiten zwischen Aufgaben, keine gemeinsame Framework-Schicht.
Neue Module sollen denselben Konventionen folgen (deutsche Docstrings, Type
Hints, reine Funktionen, dokumentiertes Fehlerverhalten).
