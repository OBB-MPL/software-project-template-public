# Release-Prozess

Dieser Ablauf beschreibt einen einfachen, reproduzierbaren Releaseprozess. Er ist bewusst technologieunabhängig und wird pro Projekt um Build-, Packaging- oder Deployment-Schritte ergänzt.

## 1. Release-Umfang prüfen

- Ziel und Umfang des zugehörigen Milestones prüfen.
- Alle für den Release vorgesehenen Issues müssen erledigt oder ausdrücklich auf einen späteren Milestone verschoben sein.
- Keine offenen Release-Blocker ignorieren.

## 2. Qualität prüfen

- Relevante automatische Tests erfolgreich ausführen.
- Stack-spezifische Build-, Lint-, Typ- und Sicherheitsprüfungen ausführen.
- Wichtige manuelle Akzeptanztests durchführen.
- Bekannte Einschränkungen dokumentieren.

Nicht ausgeführte Prüfungen ausdrücklich nennen; ein grüner Basisworkflow ersetzt keine Produktprüfung.

## 3. Dokumentation aktualisieren

Vor dem Release prüfen:

- `README.md`
- Benutzerhandbuch unter `docs/user-guide/`
- Setup- und Upgrade-Hinweise
- `CHANGELOG.md`
- relevante ADRs

Die Roadmap beschreibt zukünftige Richtung und ist kein Changelog.

## 4. Version festlegen

Semantische Versionierung verwenden, sofern das Projekt keinen begründeten anderen Standard definiert:

- `MAJOR`: inkompatible Änderungen
- `MINOR`: abwärtskompatible neue Funktionalität
- `PATCH`: abwärtskompatible Fehlerkorrekturen

Vor V1.0 können Minor-Versionen größere Entwicklungsschritte kennzeichnen.

## 5. Release-Kandidat prüfen

Der zu veröffentlichende Commit auf `main` muss dem geprüften Stand entsprechen. Nach Möglichkeit keine ungetesteten Änderungen zwischen Prüfung und Tag einfügen.

## 6. Changelog abschließen

- Einträge dem finalen Versionsstand zuordnen.
- Releasedatum ergänzen.
- Nutzerrelevante Änderungen verständlich zusammenfassen.
- Breaking Changes, Migrationen und besondere Upgrade-Schritte hervorheben.

## 7. Tag und GitHub Release erstellen

- Git-Tag auf dem geprüften Commit erstellen, z. B. `v0.1.0` oder `v1.0.0`.
- Daraus ein GitHub Release erstellen.
- Release Notes enthalten mindestens:
  - wichtigste Änderungen
  - bekannte Einschränkungen
  - erforderliche Upgrade-/Migrationsschritte
  - relevante Artefakte oder Installationshinweise

## 8. Deployment oder Verteilung

Falls das Projekt ausgeliefert oder deployed wird:

- nur aus dem getaggten/geprüften Stand bauen oder deployen
- Deployment-Ergebnis prüfen
- bei kritischen Projekten einen Rollback-Weg kennen

## 9. Milestone schließen

Den Milestone erst schließen, wenn der vereinbarte Umfang erledigt oder ausdrücklich neu zugeordnet wurde und der zugehörige Release veröffentlicht ist.

## Kurzfassung

**Milestone prüfen → Tests → Dokumentation/Changelog → Version → Tag → GitHub Release → Deployment → Milestone schließen**
