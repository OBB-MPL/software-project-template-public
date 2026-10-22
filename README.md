# Software Project Template

Schlanke, technologieunabhängige Vorlage für Markos Softwareprojekte. Sie verbindet Quellcode, langlebige Dokumentation und einen einfachen GitHub Flow.

## Status

Wiederverwendbare Projektvorlage; noch keine Anwendung. Nach dem Erstellen eines Projekts diesen Einstieg durch dessen Namen, Zweck, Zielgruppe und Reifegrad (Experiment, Alpha, Beta oder Stable) ersetzen.

Die Vorlage wurde mit KI unter Anleitung von Marko Plesinac ausgearbeitet.

## Features

- Einheitliche Dokumentationsstruktur mit Architecture Decision Records (ADRs).
- Bug- und Feature-Formulare sowie ein Pull-Request-Template.
- GitHub Issues als Single Source of Truth für konkrete Aufgaben und Akzeptanzkriterien.
- Separater Ideenspeicher für unverbindliche spätere Funktionen.
- Roadmap für geplante Entwicklungsrichtungen ohne zweite operative Aufgabenliste.
- Projects als Board, Milestones zur Release-Planung und Tags/Releases für veröffentlichte Stände.
- Projekt-Bootstrap-Checkliste für alle Einstellungen, die ein Repository-Template nicht automatisch kopiert.
- Reproduzierbarer, technologieunabhängiger Release-Prozess.
- Technologieunabhängiger Repository-Check als Ausgangspunkt für CI.

## Screenshots / Demo

Bei einem Anwendungsprojekt aussagekräftige Screenshots oder einen Demo-Link ergänzen. Diesen Abschnitt entfernen, wenn er keinen Nutzen bietet.

## Installation

1. Auf GitHub **Use this template → Create a new repository** wählen.
2. Namen und Sichtbarkeit des neuen Projekts festlegen und das Repository klonen.
3. Die [Projekt-Bootstrap-Checkliste](docs/development/project-bootstrap.md) vollständig durchgehen.
4. Die [Einrichtung](docs/development/setup.md) an den tatsächlichen Technologie-Stack anpassen und diese README projektspezifisch ausfüllen.

Die Vorlage enthält Dateien und Verzeichnisse. Labels, Project-Boards, Milestones, Secrets und Repository-Regeln müssen im neuen Repository separat eingerichtet werden. Es gibt keine automatische Synchronisierung mit späteren Änderungen der Vorlage.

## Usage

Im neuen Projekt hier den kürzesten funktionierenden Weg zur ersten Nutzung dokumentieren: Voraussetzungen, Installation, Start und ein konkretes Beispiel. Weitere Anleitungen liegen im [Benutzerhandbuch](docs/user-guide/README.md).

## Architecture

- `src/`: Anwendungscode; eine vom Framework vorgegebene Struktur ist ebenfalls zulässig.
- `tests/`: automatisierte Tests und Testhinweise.
- `scripts/`: wiederholbare Entwicklungs- und Wartungsaufgaben.
- `docs/architecture/`: Systemaufbau, Schnittstellen und Betrieb.
- `docs/development/`: Einrichtung, Tests, Projektorganisation, Bootstrap und Releaseprozess.
- `docs/user-guide/`: Installation und Nutzung.
- `docs/decisions/`: technische Entscheidungen samt Begründung.
- `docs/roadmap.md`: geplante größere Entwicklungsrichtungen.
- `docs/ideas.md`: unverbindliche Ideen für spätere Versionen.
- `.github/`: Issue-Formulare, PR-Vorlage und Workflows.

Details: [Architektur](docs/architecture/README.md) · [ADRs](docs/decisions/README.md) · [Projektorganisation](docs/development/project-management.md).

## Naming conventions

Die Vorlage verwendet absichtlich zwei Namensmuster:

- GitHub-/Community-Sonderdateien im Repository-Stamm in der üblichen Großschreibung, z. B. `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `SECURITY.md`.
- Normale Dokumentationsdateien unter `docs/` in Kleinbuchstaben mit Bindestrichen bei mehreren Wörtern, z. B. `project-management.md`, `project-bootstrap.md`, `release-process.md`.

Technisch von GitHub erwartete Pfade wie `.github/ISSUE_TEMPLATE/` und `.github/pull_request_template.md` folgen den GitHub-Konventionen.

## Development

Für den Basischeck werden Git und Python 3.10+ benötigt:

```sh
python3 scripts/check_repository.py
```

Unter Windows gegebenenfalls `py -3 scripts/check_repository.py` verwenden. Der Check prüft Textdateien auf Konfliktmarker und überflüssige Leerzeichen. Build, Produkttests und Sicherheitsprüfungen werden nach Wahl des Technologie-Stacks ergänzt; der Basischeck bestätigt keine Produktfunktion.

## Product planning

Die Ebenen sind bewusst getrennt:

1. **[Ideen](docs/ideas.md)** sammeln unreife, unverbindliche Einfälle.
2. **[Roadmap](docs/roadmap.md)** beschreibt grundsätzlich geplante Entwicklungsrichtungen.
3. **GitHub Issues** definieren konkrete Arbeit und Akzeptanzkriterien.
4. **GitHub Project** zeigt den Bearbeitungsstatus dieser Issues.
5. **Milestones** definieren den verbindlichen Umfang eines geplanten Releases.
6. **Tags und GitHub Releases** kennzeichnen veröffentlichte Stände.

Damit existiert für spätere Ideen ein eigener Ort, ohne einen zweiten Issue-Backlog zu erzeugen.

## Roadmap

Konkrete Arbeit wird ausschließlich in **GitHub Issues** geplant. Das **Project-Board** zeigt deren Bearbeitungsstatus, **Milestones** bündeln den geplanten Release-Umfang. Die langfristige Entwicklungsrichtung liegt in [docs/roadmap.md](docs/roadmap.md).

## Contributing

Der Standardablauf ist **Issue → Branch → Pull Request → Prüfung → Merge → Release bei Bedarf**. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und [Projektorganisation](docs/development/project-management.md).

Für Veröffentlichungen gilt zusätzlich der [Release-Prozess](docs/development/release-process.md).

## License

Diese Vorlage steht unter der [MIT-Lizenz](LICENSE). Sie darf auch kommerziell verwendet, angepasst und weitergegeben werden. Bei übernommenen Bestandteilen müssen die Copyright- und Lizenzhinweise erhalten bleiben.

Für eigene Inhalte und Anwendungscode eines daraus erstellten Projekts kann eine andere Lizenz gewählt werden. Die Lizenzdatei und diesen Abschnitt beim Projektstart entsprechend prüfen und anpassen.

Hinweise zum Umgang mit Schwachstellen stehen in [SECURITY.md](SECURITY.md).
