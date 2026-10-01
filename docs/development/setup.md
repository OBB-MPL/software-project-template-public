# Entwicklungsumgebung einrichten

## Vorlage übernehmen

Nach **Use this template** die folgenden Punkte einmalig bearbeiten. Dies ist eine Einrichtungsanleitung; verbleibende konkrete Arbeit als GitHub Issues erfassen.

1. README auf Projektname, Zweck, Status, Funktionen und tatsächliche Startbefehle anpassen.
2. Technologie-Stack und unterstützte Versionen auswählen; Abhängigkeiten und gegebenenfalls Lockfiles ergänzen.
3. `src/`, `tests/` und `scripts/` passend zum Stack nutzen oder nachvollziehbar anpassen. Beispieltexte entfernen, sobald echte Inhalte vorliegen.
4. `.gitignore` um tatsächliche Build-, Cache- und lokale Datenpfade ergänzen. Benötigte Konfiguration als `.env.example` ohne Geheimnisse dokumentieren.
5. GitHub Issues aktivieren; Labels, Project-Board und ersten Release-Milestone nach der [Projektorganisation](project-management.md) einrichten.
6. Repository-Regeln prüfen: PRs und erfolgreiche relevante Checks vor Merge verlangen, soweit Tarif und Arbeitsweise es unterstützen. Bei Solo-Projekten keine unerfüllbare Fremdfreigabe voraussetzen.
7. Echte Build- und Testbefehle in die CI aufnehmen. Benötigte Secrets und Umgebungen separat konfigurieren.
8. Lizenzentscheidung, Sicherheitskontakt und unterstützte Versionen festlegen.
9. Den Vorlagen-Eintrag im Changelog durch die Änderungen des neuen Projekts ersetzen.

GitHub übernimmt aus einer Repository-Vorlage die Dateien und Verzeichnisse. Project-Boards, Labels, Milestones, Berechtigungen, Secrets und Regeln separat prüfen und einrichten.

## Lokal prüfen

Für den mitgelieferten Basischeck: Git und Python 3.10+ installieren, Repository klonen und im Projektverzeichnis ausführen:

```sh
python3 scripts/check_repository.py
```

Unter Windows alternativ `py -3 scripts/check_repository.py`. Neue Dateien vor dem Check mit `git add` vormerken; geprüft werden versionierte bzw. vorgemerkte Dateien im Arbeitsverzeichnis.

Hier später die tatsächlich benötigten Befehle für Installation der Abhängigkeiten, lokalen Start, Tests und Build ergänzen. Eine neue Entwicklungsumgebung muss damit ohne mündliche Zusatzinformationen eingerichtet werden können.
