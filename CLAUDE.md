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
| Kap. 5 (S. 193–210) | Informationstheorie | *(nicht transkribiert)* |
| Anhänge A–G | Übungsaufgaben, Tabellen | `uebungen/` |

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

## Bekannte Lücken (Stand: 2026-06-16)

Folgende Inhalte aus der PDF sind noch **nicht** in den Vorlesungsdateien enthalten:

- **Kap. 1 (Einleitung)**: RC-Schaltkreis als Systembeispiel, Übertragungskette, technische Anwendungsgebiete, Literaturangaben → komplett fehlend
- **Kap. 2.1** (VL1): TikZ-Grafiken für diskrete Elementarsignale (δ[k], ε[k], Rechteck, Exponential, Sinus) fehlen noch (als `% Grafik:`-Kommentare markiert)
- **Kap. 5** (Informationstheorie, S. 193–210): Shannon-Entropie, Kanalkapazität, Huffman-Codierung → komplett fehlend
- Diverse Abbildungen in VL3–VL10 mit `% Grafik:`-Kommentaren markiert

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
├── CONTRIBUTING.md           # Box-Syntax-Referenz
├── PROGRESS.md               # Fortschrittsverfolgung
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
│   └── Vorlesung10.tex       # VL 10: Zwei ZV, Bivariate Normalvert. (Kap. 4.7)
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

## Wichtige Hinweise

- Grafiken aus den Folien werden als TikZ-Code neu erstellt, nicht als `\includegraphics` eingebunden
- Kommentare im LaTeX nur wenn absolut nötig (z. B. fehlende Grafik: `% Grafik fehlt hier`)
- Kein `\newpage` einfügen, außer es steht explizit in den Folien
- PDF kann nur in max. 20 Seiten pro `Read`-Aufruf gelesen werden
