# Mitwirken

## Aufgaben, Ideen und Entscheidungen

GitHub Issues sind die zentrale Quelle für konkrete Aufgaben, Fehler, Anforderungen und Akzeptanzkriterien. Vor neuer Arbeit vorhandene Issues prüfen. Größere Themen in verknüpfte, unabhängig prüfbare Issues aufteilen. Verbesserungen, Dokumentation, Tests und Wartung können über das Feature-/Aufgabenformular erfasst werden.

Unreife oder unverbindliche spätere Produktideen gehören zunächst in [docs/ideas.md](docs/ideas.md). Größere grundsätzlich geplante Entwicklungsrichtungen werden in [docs/roadmap.md](docs/roadmap.md) festgehalten. Sobald aus einer Idee konkrete Arbeit wird, ist das zugehörige GitHub Issue die verbindliche Quelle.

Das Project-Board visualisiert dieselben Issues. Keine parallelen TODO-Dateien oder verbindlichen Aufgabenlisten in Chats pflegen. Langlebiges Wissen liegt unter `docs/`; wesentliche technische Entscheidungen werden als [ADR](docs/decisions/README.md) festgehalten.

## GitHub Flow

1. Issue mit Problem, gewünschtem Ergebnis und prüfbaren Akzeptanzkriterien anlegen.
2. Einen kurzen Branch von aktuellem `main` erstellen, etwa `feature/42-export`, `fix/57-startup` oder `docs/61-setup`.
3. Kleine, nachvollziehbare Commits erstellen. Nur Änderungen aufnehmen, die zum Issue gehören.
4. Pull Request gegen `main` öffnen, das Issue verknüpfen und Verhalten sowie Prüfergebnisse beschreiben. `Closes #42` nur verwenden, wenn das Issue vollständig erledigt wird; sonst `Refs #42`.
5. Automatische Checks und eine inhaltliche Prüfung durchführen. Auch bei Solo-Projekten den Diff bewusst prüfen; eine unabhängige Freigabe nicht vortäuschen.
6. Nach erfolgreicher Prüfung zusammenführen, vorzugsweise per Squash Merge. Den erledigten Branch löschen und den Board-Status aktualisieren.

`main` enthält einen nachvollziehbaren, geprüften Stand. Eine dauerhafte `develop`-Branch ist nicht erforderlich. Ein Merge erzeugt nicht automatisch ein Release oder Deployment.

## Qualität

- Relevante Tests ausführen und konkrete Ergebnisse im PR festhalten; nicht ausgeführte Prüfungen benennen.
- Bei Verhaltensänderungen README, Benutzerhandbuch und Changelog nach Bedarf anpassen.
- Für neue Entscheidungen Kontext, Alternativen und Konsequenzen dokumentieren.
- Keine Zugangsdaten, privaten Schlüssel, echten Kundendaten oder lokalen Datenbanken einchecken.
- Umfang der Checks: [Testing](docs/development/testing.md).

## Releases

Ein Milestone wie `v0.1` beschreibt geplanten Umfang. Nach erfüllten Akzeptanzkriterien, relevanten Tests und dokumentierten Einschränkungen den Changelog datieren, einen Tag wie `v0.1.0` auf den geprüften Commit setzen und daraus ein GitHub Release erstellen. Release Notes nennen Änderungen, bekannte Einschränkungen und erforderliche Schritte für Aktualisierungen. Den Milestone erst schließen, wenn der vereinbarte Umfang erledigt oder ausdrücklich neu zugeordnet wurde.

Der vollständige Ablauf steht in [docs/development/release-process.md](docs/development/release-process.md).

## Neues Projekt aus der Vorlage

Nach **Use this template** die [Projekt-Bootstrap-Checkliste](docs/development/project-bootstrap.md) abarbeiten. Sie enthält insbesondere die Einstellungen, die nicht automatisch aus einem GitHub Template übernommen werden: Project, Labels, Milestones, Repository-Regeln, Secrets und Stack-spezifische CI-Prüfungen.

## Sicherheitsmeldungen

Schwachstellen und Zugangsdaten nicht in öffentlichen Issues melden. Siehe [SECURITY.md](SECURITY.md).
