# CODE.md – Skript Coding Referenz

---

## Colorboxen

Alle Boxen sind in `preamble.tex` definiert und unterstützen einen optionalen Titel-Parameter.

**Syntax:**
```tex
\begin{<umgebung>}[Optionaler Titel]
  Inhalt
\end{<umgebung>}
```

---

### Satz — rot

Für mathematische Sätze und Theoreme.

```tex
\begin{satz}[Satz von Bayes]
  $P(B \mid A) = \dfrac{P(A \mid B) \cdot P(B)}{P(A)}$
\end{satz}
```

---

### Beweis — blau

Für formale Beweise.

```tex
\begin{beweis}[Beweis: Satz von Bayes]
  Folgt direkt aus der Definition der bedingten Wahrscheinlichkeit ...
\end{beweis}
```

---

### Gedankenexperiment — lila

Für intuitive Überlegungen und Gedankenexperimente.

```tex
\begin{gedankenexperiment}[Münzwurf]
  Stellen wir uns vor, wir werfen eine faire Münze ...
\end{gedankenexperiment}
```

---

### Beispiel / Exercise — grün

Für Beispiele und Übungsaufgaben.

```tex
\begin{beispiel}[Urnenmodell]
  Eine Urne enthält 3 rote und 2 blaue Kugeln ...
\end{beispiel}
```

---

### Definition — dunkelblau

Für formale Definitionen.

```tex
\begin{definition}[Wahrscheinlichkeitsraum]
  Ein Wahrscheinlichkeitsraum ist ein Tripel $(\Omega, \mathcal{F}, P)$ ...
\end{definition}
```

---

### Bemerkung — gold

Für ergänzende Anmerkungen und Hinweise.

```tex
\begin{bemerkung}
  Dies gilt nur für endliche Wahrscheinlichkeitsräume.
\end{bemerkung}
```

---

## Mathematische Ausdrücke

Abgesetzte Formeln:
```tex
$$
1 + 1 = 2
$$
```

Inline-Formeln: `$a + b = c$`

---

## Neue Vorlesung anlegen

1. Datei `skript/VorlesungN.tex` erstellen
2. In `main.tex` die entsprechende `\include`-Zeile einkommentieren:
   ```tex
   \include{skript/VorlesungN}
   ```
