# Projektorganisation

## Eine Quelle pro Information

| Information | Verbindlicher Ort |
| --- | --- |
| Aufgabe, Fehler, Anforderung, Akzeptanzkriterien | GitHub Issue |
| Aktueller Bearbeitungsstatus | Statusfeld im GitHub Project |
| Geplanter Release-Umfang | Issue-Milestone |
| Änderung, Review und Prüfnachweis | Pull Request |
| Veröffentlichter Stand | Git-Tag und GitHub Release |
| Nutzerrelevante Änderungen | CHANGELOG.md |
| Aktueller Systemaufbau und Nutzung | README und docs/ |
| Gründe für wesentliche Entscheidungen | ADR |

Chat-Ergebnisse, die Umfang oder Akzeptanz verändern, in das betroffene Issue übertragen. Keine zweite TODO-Liste pflegen. Changelog und Release Notes fassen gelieferte Änderungen zusammen; sie verwalten keine offenen Aufgaben.

## Labels

Ein kleiner Satz reicht: `bug`, `feature`, `improvement`, `documentation`, `testing`, `maintenance`. Bei Bedarf weitere Labels begründen. Die Issue-Formulare setzen keine benutzerdefinierten Labels voraus; beim Sichten das passende Label vergeben.

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

Optional: **Priority** (`P0` dringend, `P1` hoch, `P2` normal, `P3` niedrig) und **Component** mit projektspezifischen Werten. Den Typ durch Issue-Labels abbilden. Das vorhandene Milestone-Feld für Releases anzeigen, statt ein zweites manuell gepflegtes Release-Feld anzulegen.

## Milestones und Releases

Milestones wie `v0.1` oder `v1.0` enthalten das Ziel und die zugehörigen Issues, optional einen realistischen Termin. Ein Milestone bedeutet noch keine Veröffentlichung. Tags wie `v0.1.0` kennzeichnen den exakten geprüften Commit; das GitHub Release enthält die zugehörigen Hinweise und gegebenenfalls Artefakte.

## Grenzen der Vorlage

Ein Repository-Template kopiert die Dateistruktur, richtet aber kein Project-Board und keine Milestones im neuen Projekt ein. Diese Schritte bewusst pro Projekt erledigen. Repository-Regeln, Labels und Merge-Einstellungen ebenfalls prüfen.

## Referenzen

- [GitHub: Repository aus einer Vorlage erstellen](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
