# Tests und Prüfungen

## Mitgelieferter Basischeck

`python3 scripts/check_repository.py` prüft versionierte Textdateien auf Git-Konfliktmarker und Leerzeichen am Zeilenende. Binärdateien werden übersprungen. Zwei Leerzeichen als Markdown-Zeilenumbruch sind zulässig.

Der Workflow **Repository checks** führt denselben Check bei Pushes auf `main`, bei Pull Requests gegen `main` und auf manuellen Aufruf aus. Er benötigt nur Leserechte und keine Secrets. Er prüft weder Produktverhalten noch Abhängigkeiten oder Sicherheitslücken.

## Im Projekt ergänzen

- Konkrete Befehle und Voraussetzungen für Unit-, Integrations- und gegebenenfalls Ende-zu-Ende-Tests.
- Relevante Build-, Formatierungs-, Typ- und Sicherheitsprüfungen passend zum Stack.
- Testdaten ohne personenbezogene oder produktive Inhalte.
- Manuelle Abnahme für Hardware, Betriebssysteme oder Umgebungen, die CI nicht realistisch abdeckt.

## Nachweis im Pull Request

Ausgeführten Befehl bzw. manuelle Schritte, Umgebung und Ergebnis nennen. Ausgelassene Prüfungen und verbleibende Einschränkungen ausdrücklich dokumentieren. Ein erfolgreicher Mock-Test ersetzt keine Prüfung am realen Zielsystem.
