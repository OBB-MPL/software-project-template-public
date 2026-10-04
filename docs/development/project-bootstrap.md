# Projekt-Bootstrap

Diese Checkliste wird unmittelbar nach **Use this template → Create a new repository** abgearbeitet. Ein GitHub-Template kopiert Dateien und Verzeichnisse, aber nicht automatisch alle Repository-Einstellungen, Labels, Milestones oder Project-Boards.

## 1. Projektidentität

- Repository-Namen und Beschreibung prüfen.
- README auf Projektname, Zweck, Zielgruppe und Reifegrad anpassen.
- Nicht benötigte Platzhalter und Hinweise aus dem Template entfernen.
- Sichtbarkeit des Repositorys bewusst festlegen.
- Lizenzentscheidung treffen und bei Bedarf `LICENSE` ergänzen.

## 2. Dokumentation

- `docs/architecture/` mit dem tatsächlichen Systemaufbau füllen.
- `docs/development/setup.md` an den verwendeten Technologie-Stack anpassen.
- `docs/development/testing.md` um konkrete Testbefehle und Qualitätsprüfungen ergänzen.
- `docs/roadmap.md` mit der geplanten Entwicklungsrichtung füllen.
- `docs/ideas.md` für unverbindliche spätere Ideen verwenden.
- Wesentliche technische Entscheidungen als ADR unter `docs/decisions/` dokumentieren.

## 3. GitHub Issues

- Bug- und Feature-Formulare prüfen und projektspezifisch anpassen.
- Vor dem Anlegen neuer Issues bereits vorhandene Themen prüfen.
- Konkrete Aufgaben, Fehler, Anforderungen und Akzeptanzkriterien ausschließlich als Issues führen.

Empfohlene kleine Standardmenge an Labels:

- `bug`
- `feature`
- `improvement`
- `documentation`
- `testing`
- `maintenance`

Zusätzliche Labels nur ergänzen, wenn sie im Projekt wirklich einen wiederkehrenden Nutzen haben.

## 4. GitHub Project

Für ein größeres Projekt ein GitHub Project anlegen und mit dem Repository verknüpfen.

Empfohlene Statuswerte:

- Backlog
- Ready
- In Progress
- Review / Test
- Done

Issues sind die Arbeitsobjekte; das Project visualisiert nur deren Status. Keine parallelen Project-Drafts anlegen, wenn bereits ein Issue existiert.

## 5. Milestones und Releases

- Für den nächsten geplanten Release einen Milestone anlegen, z. B. `v0.1` oder `v1.0`.
- Nur Issues zuordnen, die tatsächlich zum vereinbarten Releaseumfang gehören.
- Releaseprozess unter [release-process.md](release-process.md) prüfen.

## 6. Repository-Einstellungen

- Standardbranch auf `main` prüfen.
- Squash Merge bevorzugen.
- Nicht benötigte Merge-Methoden deaktivieren.
- Branch nach Merge automatisch löschen lassen.
- GitHub Actions aktivieren und den Basisworkflow prüfen.
- Branch Rules / Rulesets bei Bedarf ergänzen.

## 7. Sicherheit

- `SECURITY.md` projektspezifisch prüfen.
- Keine Zugangsdaten, Schlüssel, Tokens, privaten Datenbanken oder echte Kundendaten committen.
- Dependabot Alerts, Secret Scanning und Push Protection aktivieren, soweit für Repository-Typ und GitHub-Plan verfügbar.
- Bei verwendeten Paketmanagern eine projektspezifische Dependabot-Konfiguration erwägen.

## 8. CI und Qualität

Der mitgelieferte Workflow prüft nur die Repository-Basis. Danach Stack-spezifische Checks ergänzen, z. B.:

- Build
- Unit- und Integrationstests
- Linting / Formatting
- Typprüfung
- Sicherheits- oder Dependency-Checks

## 9. Erster Entwicklungszyklus

Nach dem Bootstrap gilt:

**Issue → Branch → Pull Request → Prüfung → Merge → Release bei Bedarf**

Damit ist das Projekt organisatorisch startklar.
