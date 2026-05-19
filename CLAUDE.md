# CLAUDE.md – Systemtheorie Skript

## Projekt-Überblick

LaTeX-basiertes Vorlesungsskript für **Systemtheorie 1 – Signale und Systeme I** (RUB, Prof. Dr.-Ing. Rainer Martin, SoSe 2026).

Einstiegspunkt: `main.tex`. Vorlesungen liegen in `skript/VorlesungN.tex`. Ein GitHub Workflow generiert bei Push auf `main` automatisch die PDF.

---

## Hauptaufgabe: Bilder → LaTeX transkribieren

Der User gibt jeweils:
- einen **Bildbereich** (z. B. `page_029.png – page_045.png`)
- eine **Ziel-Datei** (z. B. `skript/Vorlesung2.tex`)

### Workflow (strikt sequenziell)

1. Bild lesen (`Read` auf `vl/<ordner>/page_XXX.png`)
2. Inhalt analysieren und **wort- und formelgetreu** in LaTeX übersetzen
3. Ans Ende der Zieldatei (oder an die richtige Stelle) anfügen
4. Nächstes Bild lesen → wiederholen

**Nie mehrere Bilder auf einmal analysieren.** Ein Bild analysieren, einfügen, dann erst das nächste.

### Bildverzeichnisse

| Vorlesung | Ordner                              | Seiten      |
|-----------|-------------------------------------|-------------|
| VL 2      | `vl/systhe1_signale_vl2/`           | 029 – 059   |

Bilder sind benannt: `page_029.png`, `page_030.png`, …

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
│   ├── Vorlesung1.tex        # VL 1: Determinierte Signale
│   └── Vorlesung2.tex        # VL 2: Signaleigenschaften & Kenngrößen
└── vl/
    ├── systhe1_signale_vl2/  # PNG-Bilder VL 2 (page_029 – page_059)
    └── pdf_to_images.py      # Hilfsskript: PDF → PNG
```

---

## Wichtige Hinweise

- Transkription ist **wort- und formelgetreu** — kein Paraphrasieren, keine Ergänzungen
- Grafiken aus den Folien werden als TikZ-Code neu erstellt, nicht als `\includegraphics` eingebunden
- Kommentare im LaTeX nur wenn absolut nötig (z. B. fehlende Grafik: `% Grafik fehlt hier`)
- Kein `\newpage` einfügen, außer es steht explizit in den Folien
