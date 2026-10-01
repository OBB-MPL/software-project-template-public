# Architecture Decision Records

ADRs halten wesentliche technische Entscheidungen und ihre Gründe fest, etwa Technologieauswahl, Schnittstellen, Datenhaltung oder Betriebsmodell. Kleine Implementierungsdetails benötigen kein ADR.

1. [ADR-Vorlage](ADR-000-template.md) als `ADR-001-kurzer-titel.md` kopieren; Nummern fortlaufend vergeben.
2. Kontext, Entscheidung, Alternativen und Konsequenzen ausfüllen; Issue/PR verknüpfen.
3. Entscheidung im PR prüfen und Status auf `Accepted` setzen, sobald sie beschlossen ist.
4. Bei einer Ablösung ein neues ADR anlegen und das alte als `Superseded by ADR-XXX` kennzeichnen. Historische Begründungen erhalten.

Status: `Proposed`, `Accepted`, `Rejected`, `Superseded`. Die Vorlage `ADR-000-template.md` ist selbst keine getroffene Entscheidung. Den aktuellen Systemaufbau weiterhin unter `docs/architecture/` pflegen.
