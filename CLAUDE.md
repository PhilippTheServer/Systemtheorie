# CLAUDE.md – Systemtheorie Skript

## Projekt-Überblick

LaTeX-basiertes Vorlesungsskript für **Systemtheorie 1 – Signale und Systeme I** (RUB, Prof. Dr.-Ing. Rainer Martin, SoSe 2026).

Einstiegspunkt: `main.tex`. Vorlesungen liegen in `skript/VorlesungN.tex`. Ein GitHub Workflow generiert bei Push auf `main` automatisch die PDF.

---

## Quelldokument (Source of Truth)

**`vl/skript_SystheoEins_2025.pdf`** — Das vollständige Skript des Professors (245+ Seiten).

Beim Verbessern oder Ergänzen von Inhalten immer zuerst gegen die PDF prüfen. Die PDF kann nur in **Chunks von maximal 20 Seiten** gelesen werden:

```
Read(file_path="vl/skript_SystheoEins_2025.pdf", pages="1-20")
Read(file_path="vl/skript_SystheoEins_2025.pdf", pages="21-40")
```

### Kapitelstruktur der PDF

| PDF-Kapitel | Inhalt | VorlesungN.tex |
|-------------|--------|----------------|
| Kap. 1 (S. 9–15) | Einleitung: Signale, Systeme, Modelle, Rauschen, Information | *(nicht transkribiert)* |
| Kap. 2.1 (S. 17–61) | Determinierte Signale | VL1.tex + VL2.tex |
| Kap. 2.2 (S. 62–72) | Zufällige Signale | VL3.tex |
| Kap. 2.3 (S. 73–86) | Analog-Digital-Umsetzung | VL4.tex |
| Kap. 3 (S. 89–131) | Systeme und ihre Eigenschaften | VL5.tex + VL6.tex |
| Kap. 4 (S. 133–191) | Wahrscheinlichkeitsrechnung | VL7.tex – VL10.tex |
| Kap. 5 (S. 193–210) | Informationstheorie | VL11.tex |
| Anhänge A–G | Übungsaufgaben, Tabellen | `Uebung/` |

---

## Themen lokalisieren

Alle nummerierten `\chapter{}`, `\section{}` und `\subsection{}` tragen ein `\label{}`. Damit lässt sich jedes Thema mit einem einzigen Befehl finden:

```bash
grep -rn "label{sec:" skript/          # alle Abschnitte
grep -rn "label{chap:" skript/         # alle Kapitel
grep -rn "label{sec:normalverteilung" skript/  # konkretes Thema → Datei + Zeile
```

Stern-Varianten (`\section*{}`, `\subsection*{}`) haben **kein** Label.

---

## Bekannte Lücken (Stand: 2026-07-14)

Folgende Inhalte aus der PDF sind noch **nicht** in den Vorlesungsdateien enthalten:

- **Kap. 1 (Einleitung)**: RC-Schaltkreis als Systembeispiel, Übertragungskette, technische Anwendungsgebiete, Literaturangaben → komplett fehlend
- **Kap. 2.1** (VL1): TikZ-Grafiken für diskrete Elementarsignale (δ[k], ε[k], Rechteck, Exponential, Sinus) fehlen noch (als `% Grafik:`-Kommentare markiert)
- Diverse Abbildungen in VL3–VL11 mit `% Grafik:`-Kommentaren markiert

**Nicht mehr offen:** Kap. 5 (Informationstheorie) galt hier lange als „komplett fehlend".
Das stimmt seit VL11 nicht mehr — `skript/Vorlesung11.tex` deckt Informationsmaß, Entropie,
Redundanz, Kanalkapazität, Shannon/Fano, Huffman, Lauflängencodierung und Kullback-Leibler ab
und ist in `main.tex` eingebunden. Auch `formelsammlung.tex` und `Uebung/uebung11.tex` haben es.
Das ist klausurrelevant: Aufgabe 4 jeder Klausur ist Informationstheorie, also 25 von 100 Punkten.

---

## LaTeX-Konventionen

### Mathematik

Abgesetzte Formeln – **immer** mit Leerzeilen davor und danach:
```tex
$$
1 + 1 = 2
$$
```

Inline-Formeln: `$a + b = c$`

**Wichtige Notation:**
- Komplexwertige Signale: `$\underline{x}(t)$` (mit Unterstrich, nicht `$x*(t)$`)
- Konjugiertes Signal: `$\underline{x}^*(t)$` (nicht `$x*(t)$`)
- Zeitdiskretes Signal: `$x[k]$`, `$k \in \mathbb{Z}$`
- Realteil/Imaginärteil: `$\operatorname{Re}\{...\}$`, `$\operatorname{Im}\{...\}$`
- Betrag: `$|\underline{x}(t)|$`
- Argument: `$\arg\{x(t)\}$`

### Farbige Boxen (definiert in `preamble.tex`)

Alle Boxen haben einen **optionalen Titel**:

```tex
\begin{<umgebung>}[Optionaler Titel]
  Inhalt
\end{<umgebung>}
```

| Umgebung           | Farbe      | Verwendung                        |
|--------------------|------------|-----------------------------------|
| `definition`       | blau       | Formale Definitionen              |
| `satz`             | rot        | Sätze und Theoreme                |
| `beweis`           | blau       | Formale Beweise                   |
| `gedankenexperiment` | lila     | Intuitive Überlegungen            |
| `beispiel`         | grün       | Beispiele und Übungsaufgaben      |
| `bemerkung`        | gold       | Ergänzende Anmerkungen            |

### Grafiken

Grafiken werden mit **TikZ / pgfplots** neu erstellt (nicht als Bild eingebettet). Pakete sind in `preamble.tex` geladen (`tikz`, `pgfplots`, `pgfplotslibrary{groupplots}`).

Fehlende Grafiken mit Kommentar kennzeichnen:
```tex
% Grafik: Beschreibung der fehlenden Grafik
```

### Struktur

```tex
\chapter{Kapitelname}
\section{Abschnitt}
\subsection{Unterabschnitt}
\subsection*{Unterabschnitt ohne Nummerierung}
```

---

## Neue Vorlesung anlegen

1. `skript/VorlesungN.tex` erstellen, beginnend mit `\chapter{...}`
2. In `main.tex` die `\include`-Zeile einkommentieren:
   ```tex
   \include{skript/VorlesungN}
   ```

---

## Projektstruktur

```
.
├── main.tex                  # Einstiegspunkt
├── preamble.tex              # Pakete, Farben, Box-Umgebungen
├── formelsammlung.tex        # Grundlage der handschriftlichen Klausur-Formelsammlung
├── CONTRIBUTING.md           # Box-Syntax-Referenz
├── PROGRESS.md               # VERALTET – Fortschritt liegt in Linear (s. u.)
├── Klausuren/                # 19 Altklausuren + 8 Miniklausuren – LOKAL, nicht versioniert
├── skript/
│   ├── Vorlesung1.tex        # VL 1: Determinierte Signale (Kap. 2.1.1–2.1.5)
│   ├── Vorlesung2.tex        # VL 2: Signaleigenschaften, KKF, Fourier (Kap. 2.1.6–2.1.8)
│   ├── Vorlesung3.tex        # VL 3: Zufällige Signale (Kap. 2.2)
│   ├── Vorlesung4.tex        # VL 4: Abtastung & Quantisierung (Kap. 2.3)
│   ├── Vorlesung5.tex        # VL 5: Systeme & Eigenschaften (Kap. 3.1–3.2)
│   ├── Vorlesung6.tex        # VL 6: LTI-Systeme, Faltung, DPCM (Kap. 3.3–3.5)
│   ├── Vorlesung7.tex        # VL 7: Wahrscheinlichkeit, Axiome (Kap. 4.1–4.2)
│   ├── Vorlesung8.tex        # VL 8: Bedingte W., Satz von Bayes (Kap. 4.3)
│   ├── Vorlesung9.tex        # VL 9: Zufallsvariablen, Verteilungen (Kap. 4.4–4.6)
│   ├── Vorlesung10.tex       # VL 10: Zwei ZV, Bivariate Normalvert. (Kap. 4.7)
│   └── Vorlesung11.tex       # VL 11: Informationstheorie (Kap. 5)
├── Uebung/
│   └── uebung1.tex … uebung11.tex   # Übungsblätter, vollständig ausgearbeitet
└── vl/
    ├── skript_SystheoEins_2025.pdf  # Professorskript (Source of Truth)
    └── pdf_to_images.py              # Hilfsskript: PDF → PNG
```

---

## Git-Workflow (immer einhalten)

Nach **jeder** Änderung an Dateien diesen Workflow vollständig durchführen:

1. **Branch erstellen** — `git checkout -b feat/<kurzbeschreibung>`
2. **Commit** — aussagekräftige Commit-Message mit `feat/fix/chore`-Präfix
3. **Push** — `git push -u origin <branch>`
4. **Pull Request erstellen** — `gh pr create` mit Titel und kurzer Beschreibung
5. **Merge** — `gh pr merge --merge` (kein Squash, kein Rebase)
6. **Branch löschen** — `git branch -d <branch>` lokal + `git push origin --delete <branch>`

Direkte Commits auf `main` sind **verboten**.

---

## Rechenaufgaben-Format (PFLICHT)

Jede Rechenaufgabe **muss** in folgender Struktur beantwortet werden:

| Abschnitt | Inhalt |
|-----------|--------|
| **Gegeben** | Alle bekannten Größen, Voraussetzungen, Versuchsbeschreibung |
| **Gesucht** | Die zu berechnende Wahrscheinlichkeit / Größe, klar formuliert |
| **Formel** | Die verwendete Formel mit Referenz auf Label im Skript (z. B. `\ref{sec:kombinatorik}`) |
| **Rechnung** | Vollständige, nachvollziehbare Rechenschritte |
| **Lösung** | Ergebnis in Bruch und Dezimalform, ggf. kurze Interpretation |

Diese Struktur ist **obligatorisch** – keine Ausnahmen.

---

## Lernplanung & Fortschritt → Linear

**Linear ist die Source of Truth für Lernfortschritt, Aufgaben und Workload.** Nicht `PROGRESS.md`.

- Workspace `philipp-ui`, Team **Uni** (`UNI`), Projekt **Systemtheorie**
- **Klausur: Di, 18.08.2026**, 120 min, 100 P, 4 Aufgaben à 25 P
- Hilfsmittel: nicht-programmierbarer TR + **handschriftliche Formelsammlung, max. 2 DIN-A4-Blätter beidseitig**

### Done-Definition (gilt für alle Themen-Issues)

> Ein Thema ist **Done**, wenn eine Aufgabe dazu **ohne Lösungsblick gerechnet** wurde — nicht, wenn es gelesen wurde.

### Priorisierung

Aus einer Frequenzanalyse aller 19 Altklausuren (Linear-Dokument „Frequenzanalyse: was kommt wirklich dran").
Label `frequenz/*` zählt Vorkommen in den **12 Klausuren ab 2019**; die 7 älteren (2014–2018) prüfen ein
anderes Format und zählen nicht. Label `konfidenz/*` kommt aus der Diagnose.
Reihenfolge: **rot × immer** zuerst.

**Kam seit 2019 in 0 von 12 Klausuren vor** — nicht dafür lernen, nicht dafür ausarbeiten:
Fourierreihe, Amplituden-/Phasenspektrum, Parseval/Gibbs, Aliasing, Kombinatorik, Bayes.

### `PROGRESS.md`

Veraltet und wird **nicht** gepflegt. Die Datei behauptet, fast nichts sei fertig, obwohl alle 11
Vorlesungen ausgearbeitet sind. Sie zählt außerdem Stoff auf, der klausurirrelevant ist.
Nicht als Fortschrittsquelle heranziehen.

### `Klausuren/`

19 Altklausuren + 8 Miniklausuren, **lokal und bewusst nicht versioniert** (`.gitignore`).
Dieses Repo ist **öffentlich**; die Klausuren sind Lehrstuhlmaterial inkl. Musterlösungen und
enthalten eigene korrigierte Arbeiten. Nicht committen.

Design-Spec: `docs/superpowers/specs/2026-07-14-linear-lernplan-design.md`

---

## Wichtige Hinweise

- Grafiken aus den Folien werden als TikZ-Code neu erstellt, nicht als `\includegraphics` eingebunden
- Kommentare im LaTeX nur wenn absolut nötig (z. B. fehlende Grafik: `% Grafik fehlt hier`)
- Kein `\newpage` einfügen, außer es steht explizit in den Folien
- PDF kann nur in max. 20 Seiten pro `Read`-Aufruf gelesen werden
