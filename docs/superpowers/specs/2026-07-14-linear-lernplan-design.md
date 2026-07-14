# Linear-Lernplan Systemtheorie — Design

**Stand:** 2026-07-14 · **Klausur:** 2026-08-18 (Di) · **Restzeit:** 35 Tage
**Kapazität:** ~30–40 h/Woche (Vollzeit) → ~150–200 h Gesamtbudget

---

## Ausgangslage

Vierter Prüfungsversuch. Drei vom Nutzer selbst benannte Scheiterpunkte:

1. Bestimmte Themen sitzen nicht
2. Rechnen unter Zeitdruck
3. Nie genug gelernt / Dranbleiben

Zwei davon sind **keine Wissensprobleme**. Ein reiner Stoffdurchlauf adressiert nur den ersten
und wiederholt im Wesentlichen, was in drei Versuchen schon dreimal gemacht wurde. Jeder
Scheiterpunkt bekommt deshalb ein eigenes Instrument.

| Scheiterpunkt | Instrument |
|---|---|
| Themen sitzen nicht | Konfidenz-Labels, gesetzt durch echte Diagnose statt Selbsteinschätzung |
| Rechnen unter Zeitdruck | ~15 Klausursätze, ab Phase 3 drei pro Woche unter Uhr |
| Dranbleiben | Fälligkeitsdaten je Issue, Wochen-Cycles, wöchentliches Status-Update |

## Bestand

**Linear:** Team `Uni` (UNI), Projekt `Systemtheorie` (Urgent) existiert bereits.
Enthält nur 13 `Quiz N`-Issues unter Milestone *Quiz* — Quiz 1–4 Done, Quiz 5–13 Canceled.
Kein Stoff, keine Übungen, keine Klausuren abgebildet. Keine Cycles aktiv.

**Repo:** 11 Vorlesungen (`skript/`), 11 ausgearbeitete Übungslösungen (`Uebung/`),
Formelsammlung, Professorskript (`vl/skript_SystheoEins_2025.pdf`),
`Saal_Aufgaben.pdf` + `Gruppen_Aufgaben.pdf` (je 48 S.).

**Klausuren (`Klausuren/`, lokal, nicht versioniert):** 28 PDFs + 12 JPGs über 15 Semester.
Netto ~15 verwertbare Sätze, die meisten 15–18 S. mit **integrierten Lösungen**.
Bekannte Mängel: `Ab 2014-2017` ist ein Sammel-PDF, kein Einzelsatz · WS 18-19 fehlt ·
SS 24 nur als WhatsApp-Fotos · Dubletten (`Copy of …`) · Fehlablage (SS-2019-PDF im Ordner `SS 20`) ·
`SS 22/Klausur.pdf` hat nur 1 Seite, vermutlich unbrauchbar.
Dazu 5 **Miniklausuren** — kurz, ideal als tägliches Zeit-Aufwärmen.

## Entscheidungen

| Frage | Entscheidung | Begründung |
|---|---|---|
| Zieldatum Projekt | 24.07. → **18.08.** | Stand auf dem Semesterende, nicht auf dem Klausurtermin |
| Fortschritts-Quelle | **Linear** ist Source of Truth | `PROGRESS.md` hat 3 Häkchen, obwohl alle 11 VL fertig sind — doppelte Buchführung führt dazu, dass beide Seiten falsch sind |
| Klausur-PDFs im Git | **Nein**, `.gitignore` | Repo ist **öffentlich**. Lehrstuhlmaterial + abfotografierte Klausur + eigene korrigierte Miniklausur mit möglichen Personendaten. Für den Lernplan kein Funktionsverlust |
| Professorskript (bereits public) | vorerst belassen | Bekanntes Risiko, Klausur hat Vorrang. Nach dem 18.08. neu bewerten |
| Wochen-Cycles | **Ja**, teamweit | Stärkster Taktgeber gegen das Dranbleib-Problem |
| Granularität | ~30 Themen-Issues, nicht ~100 | Sonst verwaltet man mehr, als man lernt |

### Done-Definition (Kern des Designs)

> Ein Thema ist **Done**, wenn eine Aufgabe dazu **ohne Lösungsblick gerechnet** wurde.
> Nicht, wenn es gelesen wurde.

Bei drei Fehlversuchen ist „gelesen = Done" die Falle, die ein Board grün färbt, während in
der Klausur nichts abrufbar ist. Diese Definition ist nicht verhandelbar; sie steht in der
Projektbeschreibung und in jeder Issue-Vorlage.

## Struktur

Vier **Milestones** = Zeitphasen (nicht Stoffblöcke — Stoffblöcke hätten keinen Ort für
„Rechnen unter Zeitdruck"):

| # | Milestone | Zeitraum | Inhalt |
|---|---|---|---|
| 1 | **Diagnose** | Di 14.07. – Fr 17.07. | 2 Altklausuren unter echten Bedingungen, ungelernt. Parallel: Frequenzanalyse aller ~15 Sätze |
| 2 | **Lücken schließen** | Sa 18.07. – Mo 03.08. | Themen-Issues nach Priorität = Klausurfrequenz × Konfidenz |
| 3 | **Klausurtraining** | Di 04.08. – Fr 14.08. | 3 Sätze/Woche unter Uhr + Miniklausur als tägliches Aufwärmen |
| 4 | **Endspurt** | Sa 15.08. – Mo 17.08. | Formelsammlung, verbliebene rote Themen, **kein neuer Stoff** |

Der bestehende Milestone *Quiz* bleibt unangetastet (historisch, abgeschlossen).

### Frequenzanalyse (Phase 1, der eigentliche Hebel)

15 Klausuren desselben Lehrstuhls über 12 Jahre erlauben **Priorisierung aus Empirie statt
aus Bauchgefühl**. Ausgezählt wird pro Thema, in wie vielen Terminen es vorkam. Bei 35 Tagen
entscheidet Priorisierung mehr über das Bestehen als Lernmenge: „rot **und** kommt immer dran"
zuerst, „grün **und** kam nie dran" gar nicht.

Ergebnis wird als Linear-Dokument im Projekt abgelegt (Themen × Semester-Matrix).

### Issues (~50)

- **~4 Diagnose** — 2 Klausuren schreiben, Auswertung, Frequenzanalyse
- **~30 Themen** — verdichtet aus `PROGRESS.md`, je mit Label `konfidenz/*` + `frequenz/*`,
  Verweis auf `skript/VorlesungN.tex` (Label) und passende Übungsaufgaben
- **~15 Klausursätze** — je ein Issue, Pfad zum PDF, Soll-Zeit, Ergebnis als Kommentar

### Labels (neu anzulegen)

- `konfidenz/rot` · `konfidenz/gelb` · `konfidenz/gruen` — gesetzt durch Diagnose, laufend gepflegt
- `frequenz/immer` · `frequenz/oft` · `frequenz/selten` — Ergebnis der Frequenzanalyse
- `altklausur` · `theorie` · `rechnen` — Arbeitstyp

Bestehende Labels (`exercise`, `Lecture`, `repetition`) werden wiederverwendet, wo sie passen.

## Laufender Betrieb (was „Management übernehmen" heißt)

- **Nach jeder Lerneinheit:** Issues auf Done, Konfidenz-Label nachziehen
- **Wöchentlich:** Projekt-Status-Update in Linear (`save_status_update`) mit Health-Ampel —
  geschriebene Klausuren, verschobene Konfidenz, Restpensum vs. Restzeit
- **Nach jeder geschriebenen Klausur:** Ergebnis als Kommentar, Fehlerthemen zurück auf rot,
  Priorisierung der Restphase anpassen
- **Bei Verzug:** Umpriorisieren statt Nachtschichten — der Plan wird gekürzt, nicht der Schlaf

## Bewusst nicht im Scope

- Sanierung der Git-History (Professorskript) — nach der Klausur
- Aufräumen der Klausur-Dubletten/Fehlablagen — nur wenn es beim Rechnen stört
- Elektrotechnik und Wafi — eigene Projekte, hier nicht angefasst
- Aktualisierung von `PROGRESS.md` — wird durch Linear ersetzt, nicht gepflegt

## Offene Punkte

1. **Cycles muss der Nutzer selbst aktivieren** — die Linear-Integration bietet nur
   Lesezugriff (`list_cycles`), kein Tool für Team-Einstellungen.
   *Settings → Team Uni → Cycles → Enable*, Länge 1 Woche.
   Der Plan funktioniert über Fälligkeitsdaten auch ohne; Issues sortieren sich nachträglich ein.
2. **Welche 2 Klausuren für die Diagnose?** Vorschlag: SS 25 und WS 24-25 — die jüngsten,
   also am nächsten am erwarteten Format.
3. `SS 22/Klausur.pdf` (1 Seite) vor Phase 3 prüfen und ggf. aussortieren.
