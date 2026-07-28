# Kontext

## Ziel

`test` dient der autodev-Pipeline als Benchmark-Projekt: Jede Aufgabe ist ein
kleines, klar abgegrenztes Python-Modul, dessen korrekte Implementierung
allein durch die mitgelieferten pytest-Tests bewiesen wird. Das Repo bleibt
bewusst einfach (flach, abhängigkeitsarm), damit Aufgaben isoliert und
automatisiert bearbeitbar sind.

## Konventionen

- **Ein Modul pro Aufgabe**: `<modul>.py` + `test_<modul>.py` im Repo-Root
  mit gleicher Namensbasis. Module bleiben voneinander unabhängig
  (keine Querimporte).
- **Tests sind die Spezifikation**: `test_<modul>.py` (pytest) definiert den
  Vertrag inklusive Fehlerfälle. Implementierungen müssen die Tests
  unverändert bestehen; Tests werden nie an eine Implementierung angepasst.
- **Vertrags-Docstring**: Jedes Aufgabenmodul trägt seinen Vertrag im
  Modul-Docstring samt dem Hinweis „Ändere NUR diese Datei" – eine Aufgabe
  ändert nur die in ihrer Beschreibung genannten Dateien.
- **Stub-Einstieg**: Neue Aufgabenmodule werden als Stub
  (`raise NotImplementedError`) mit vollständigem Vertrag im Docstring und
  fertigen Tests angelegt.
- **Reine Funktionen**: Keine Seiteneffekte, Eingaben werden nicht mutiert,
  Fehler über Ausnahmen (`ValueError`, `KeyError`).
- **Sprache**: Code-Kommentare, Docstrings und Doku auf Deutsch. Die
  bestehenden Modul-Docstrings schreiben Umlaute als ae/oe/ue – neue Module
  halten sich an diesen Stil.

## Constraints

- Nur Python-Standardbibliothek; einzige externe Abhängigkeit ist pytest
  (Test-Abhängigkeit, nicht Laufzeit).
- Keine Paketstruktur, kein Build-Schritt, keine Runtime-Abhängigkeiten.
- `index.html` bleibt eigenständig und statisch (kein JavaScript, kein
  Backend).
- Verifikation erfolgt ausschließlich über pytest
  (`pytest test_<modul>.py`).

## Richtung

Weitere Aufgabenmodule folgen demselben Muster (Stub + Vertrags-Docstring +
pytest-Tests). Die Doku (`docs/ARCHITEKTUR.md` und diese Datei) wird bei
jeder Änderung an Modulen, Schnittstellen oder Konventionen mitgepflegt und
enthält nur Dauerhaftes: Aufbau, Zusammenspiel, Schnittstellen, Konventionen,
Ziel – keinen Entwicklungsstand und keine TODO-Listen (der aktuelle Stand
lebt im Board, nicht in Dateien).
