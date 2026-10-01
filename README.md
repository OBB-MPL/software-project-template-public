# Software Project Template

Schlanke, technologieunabhängige Vorlage für Markos Softwareprojekte. Sie verbindet Quellcode, langlebige Dokumentation und einen einfachen GitHub Flow.

## Status

Wiederverwendbare Projektvorlage; noch keine Anwendung. Nach dem Erstellen eines Projekts diesen Einstieg durch dessen Namen, Zweck, Zielgruppe und Reifegrad (Experiment, Alpha, Beta oder Stable) ersetzen.

## Features

- Einheitliche Dokumentationsstruktur mit Architecture Decision Records (ADRs).
- Bug- und Feature-Formulare sowie ein Pull-Request-Template.
- GitHub Issues als Single Source of Truth für Aufgaben und Akzeptanzkriterien.
- Projects als Board, Milestones zur Release-Planung und Tags/Releases für veröffentlichte Stände.
- Technologieunabhängiger Repository-Check als Ausgangspunkt für CI.

## Screenshots / Demo

Bei einem Anwendungsprojekt aussagekräftige Screenshots oder einen Demo-Link ergänzen. Diesen Abschnitt entfernen, wenn er keinen Nutzen bietet.

## Installation

1. Auf GitHub **Use this template → Create a new repository** wählen.
2. Namen und Sichtbarkeit des neuen Projekts festlegen und das Repository klonen.
3. Die [Einrichtung](docs/development/setup.md) durchgehen und diese README projektspezifisch ausfüllen.

Die Vorlage enthält Dateien und Verzeichnisse. Labels, Project-Boards, Milestones, Secrets und Repository-Regeln müssen im neuen Repository separat eingerichtet werden. Es gibt keine automatische Synchronisierung mit späteren Änderungen der Vorlage.

## Usage

Im neuen Projekt hier den kürzesten funktionierenden Weg zur ersten Nutzung dokumentieren: Voraussetzungen, Installation, Start und ein konkretes Beispiel. Weitere Anleitungen liegen im [Benutzerhandbuch](docs/user-guide/README.md).

## Architecture

- `src/`: Anwendungscode; eine vom Framework vorgegebene Struktur ist ebenfalls zulässig.
- `tests/`: automatisierte Tests und Testhinweise.
- `scripts/`: wiederholbare Entwicklungs- und Wartungsaufgaben.
- `docs/architecture/`: Systemaufbau, Schnittstellen und Betrieb.
- `docs/development/`: Einrichtung, Tests und Arbeitsablauf.
- `docs/user-guide/`: Installation und Nutzung.
- `docs/decisions/`: technische Entscheidungen samt Begründung.
- `.github/`: Issue-Formulare, PR-Vorlage und Workflows.

Details: [Architektur](docs/architecture/README.md) · [ADRs](docs/decisions/README.md).

## Development

Für den Basischeck werden Git und Python 3.10+ benötigt:

```sh
python3 scripts/check_repository.py
```

Unter Windows gegebenenfalls `py -3 scripts/check_repository.py` verwenden. Der Check prüft Textdateien auf Konfliktmarker und überflüssige Leerzeichen. Build, Produkttests und Sicherheitsprüfungen werden nach Wahl des Technologie-Stacks ergänzt; der Basischeck bestätigt keine Produktfunktion.

## Roadmap

Konkrete Arbeit wird ausschließlich in **GitHub Issues** geplant. Das **Project-Board** zeigt deren Bearbeitungsstatus, **Milestones** bündeln den geplanten Release-Umfang. Hier nur langfristige Ziele und Links auf diese Ansichten ergänzen; keine zweite Aufgabenliste führen.

## Contributing

Der Standardablauf ist **Issue → Branch → Pull Request → Prüfung → Merge → Release bei Bedarf**. Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und [Projektorganisation](docs/development/project-management.md).

## License

Diese Vorlage legt keine Lizenz für künftige Projekte fest. Vor externer Weitergabe die passende Lizenzentscheidung treffen, gegebenenfalls eine `LICENSE` ergänzen und diesen Abschnitt aktualisieren. Hinweise zum Umgang mit Schwachstellen stehen in [SECURITY.md](SECURITY.md).
