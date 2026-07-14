# Fortschritt → Linear

**Diese Datei wird nicht mehr gepflegt.** Der Lernfortschritt liegt in Linear:

**Team Uni · Projekt Systemtheorie** — https://linear.app/philipp-ui/project/systemtheorie-b592a834beba

---

## Warum

Die frühere Checkliste hier war irreführend. Sie zeigte drei Häkchen bei rund 100 Punkten, obwohl
alle 11 Vorlesungen ausgearbeitet und gemerged sind — doppelte Buchführung führt zuverlässig dazu,
dass beide Seiten falsch sind.

Zweitens war sie nach der **Stoffgliederung** sortiert, nicht nach Klausurrelevanz. Eine Auswertung
aller 19 Altklausuren (2014–2025) zeigt, dass ein erheblicher Teil dieser Gliederung nie geprüft
wurde — die Fourierreihe zum Beispiel in keiner einzigen Klausur. Eine Liste, die Fourierreihe und
Faltung gleich gewichtet, ist als Lernplan schädlich.

## Was stattdessen gilt

| | |
|---|---|
| **Klausur** | Di, 18.08.2026 · 120 min · 100 P · 4 Aufgaben à 25 P |
| **Hilfsmittel** | Nicht-programmierbarer TR + handschriftliche Formelsammlung, max. 2 DIN-A4-Blätter beidseitig |
| **Done heißt** | Aufgabe ohne Lösungsblick gerechnet — nicht: gelesen |
| **Priorisierung** | `frequenz/*` × `konfidenz/*`, rot × immer zuerst |

Klausuraufbau, in allen 19 ausgewerteten Altklausuren identisch:

| Aufgabe | Thema | Punkte |
|---|---|---|
| 1 | Zeitkontinuierliches LTI: Impulsantwort, Kausalität, BIBO, Faltung | 25 |
| 2 | Zeitdiskret: Differenzengleichung, Blockdiagramm, BIBO | 25 |
| 3 | Stetige Zufallsvariable: WDF/CDF, E{X}, var{X}, Transformation | 25 |
| 4 | Informationstheorie: Entropie + Huffman/Fano + Beweis | 25 |

Vollständige Auszählung: Linear-Dokument „Frequenzanalyse: was kommt wirklich dran".
Design-Entscheidungen: `docs/superpowers/specs/2026-07-14-linear-lernplan-design.md`.

## Skript-Ausarbeitung

Alle 11 Vorlesungen sind ausgearbeitet und in `main.tex` eingebunden, inklusive VL11
(Informationstheorie). Offen sind nur noch TikZ-Grafiken, die in den `.tex`-Dateien als
`% Grafik:`-Kommentare markiert sind — siehe „Bekannte Lücken" in `CLAUDE.md`.
