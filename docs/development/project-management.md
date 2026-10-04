# Projektorganisation

## Eine Quelle pro Information

| Information | Verbindlicher Ort |
| --- | --- |
| Unverbindliche spätere Idee | `docs/ideas.md` |
| Größere geplante Entwicklungsrichtung | `docs/roadmap.md` |
| Konkrete Aufgabe, Fehler, Anforderung, Akzeptanzkriterien | GitHub Issue |
| Aktueller Bearbeitungsstatus | Statusfeld im GitHub Project |
| Geplanter Release-Umfang | Issue-Milestone |
| Änderung, Review und Prüfnachweis | Pull Request |
| Veröffentlichter Stand | Git-Tag und GitHub Release |
| Nutzerrelevante Änderungen | `CHANGELOG.md` |
| Aktueller Systemaufbau und Nutzung | `README.md` und `docs/` |
| Gründe für wesentliche Entscheidungen | ADR unter `docs/decisions/` |

Chat-Ergebnisse, die Umfang oder Akzeptanz verändern, in das betroffene Issue übertragen. Keine zweite TODO-Liste pflegen. Changelog und Release Notes fassen gelieferte Änderungen zusammen; sie verwalten keine offenen Aufgaben.

## Ideen, Roadmap und Issues

Die drei Ebenen haben unterschiedliche Aufgaben:

1. **Ideen** sind unverbindlich. Sie dürfen unfertig, experimentell oder weit in der Zukunft liegen.
2. **Roadmap** beschreibt größere Entwicklungsrichtungen, die grundsätzlich verfolgt werden sollen, aber noch keinen verbindlichen Releaseumfang darstellen.
3. **Issues** enthalten konkrete, umsetzbare Arbeit mit ausreichend Kontext und bei Bedarf Akzeptanzkriterien.

Der typische Weg lautet:

**Idee → Bewertung → Roadmap und/oder Issue → Milestone → Umsetzung → Release**

Nicht jede Idee muss umgesetzt oder in die Roadmap aufgenommen werden. Nicht jeder Roadmap-Punkt braucht sofort ein Issue.

## Labels

Ein kleiner Satz reicht:

- `bug`
- `feature`
- `improvement`
- `documentation`
- `testing`
- `maintenance`

Bei Bedarf weitere Labels begründen. Die Issue-Formulare setzen keine benutzerdefinierten Labels voraus; beim Sichten das passende Label vergeben.

Komponenten- oder Prioritätslabels nur einführen, wenn sie regelmäßig Mehrwert bringen. Für Priorität kann alternativ ein eigenes Project-Feld verwendet werden.

## Project als Board

Für jedes größere Projekt ein GitHub Project auf Konto- oder Organisationsebene erstellen, mit dem Repository verknüpfen und eine Board-Ansicht nach **Status** anlegen:

| Status | Bedeutung |
| --- | --- |
| Backlog | Erfasst, noch nicht zur Bearbeitung vorbereitet |
| Ready | Ziel und Akzeptanzkriterien klar, nächste Arbeit ausgewählt |
| In Progress | Umsetzung läuft |
| Review / Test | PR oder Ergebnis wird geprüft |
| Done | Akzeptanzkriterien erfüllt und Änderung übernommen |

Issues in das Board aufnehmen; keine zweite Aufgabe als Project-Draft anlegen, wenn bereits ein Issue existiert. PRs mit Issues verknüpfen. Automationen für Hinzufügen und Abschluss können später eingerichtet werden; anfangs reicht bewusstes Aktualisieren.

Optional: **Priority** (`P0` dringend, `P1` hoch, `P2` normal, `P3` niedrig) und **Component** mit projektspezifischen Werten. Das vorhandene Milestone-Feld für Releases anzeigen, statt ein zweites manuell gepflegtes Release-Feld anzulegen.

## Milestones und Releases

Milestones wie `v0.1` oder `v1.0` enthalten das Ziel und die zugehörigen Issues, optional einen realistischen Termin. Ein Milestone bedeutet noch keine Veröffentlichung. Tags wie `v0.1.0` kennzeichnen den exakten geprüften Commit; das GitHub Release enthält die zugehörigen Hinweise und gegebenenfalls Artefakte.

Der standardisierte Ablauf ist unter [release-process.md](release-process.md) dokumentiert.

## Namenskonventionen

- GitHub-/Community-Sonderdateien im Repository-Stamm: übliche Großschreibung wie `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `SECURITY.md`.
- Normale Dokumentation unter `docs/`: Kleinbuchstaben, bei mehreren Wörtern Bindestriche, z. B. `project-management.md`, `project-bootstrap.md`, `release-process.md`.
- Verzeichnisse: Kleinbuchstaben, bei Bedarf Bindestriche, z. B. `user-guide/`.
- GitHub-spezifische Pfade folgen den von GitHub erwarteten Konventionen, z. B. `.github/ISSUE_TEMPLATE/` und `.github/pull_request_template.md`.

Diese Konvention dient vor allem Konsistenz und Portabilität; projektspezifische Framework-Strukturen dürfen ihren üblichen Konventionen folgen.

## Grenzen der Vorlage

Ein Repository-Template kopiert die Dateistruktur, richtet aber kein Project-Board und keine Milestones im neuen Projekt ein. Diese Schritte bewusst pro Projekt erledigen. Repository-Regeln, Labels und Merge-Einstellungen ebenfalls prüfen.

Dafür dient die [Projekt-Bootstrap-Checkliste](project-bootstrap.md).

## Referenzen

- [GitHub: Repository aus einer Vorlage erstellen](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
