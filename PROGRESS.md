# Skript-Fortschritt – Systemtheorie 1 (141170)

**Dozent:** Prof. Dr.-Ing. Rainer Martin · RUB · SoSe 2026

**Legende:**
- `[ ]` Noch nicht begonnen
- `[~]` In Bearbeitung / Skizze vorhanden
- `[x]` Vollständig ausgearbeitet

---

## Block 1 · Signale und Systeme

### 1.1 Grundbegriffe und Klassifikation von Signalen
- [x] Definition: Signal, Determinismus vs. Stochastik
- [x] Klassifikation nach Wertebereich (kontinuierlich / diskret / digital)
- [x] Klassifikation nach Zeitbereich (zeitkontinuierlich / zeitdiskret)
- [ ] Energie und Leistung eines Signals
  - [ ] Energie-Definition und Berechnung
  - [ ] Leistungs-Definition und Berechnung
  - [ ] Energie- vs. Leistungssignale
- [ ] Periodizität
  - [ ] Definition periodisches Signal
  - [ ] Grundperiode $T_0$ bestimmen
- [ ] Symmetrieeigenschaften
  - [ ] Gerades Signal (Achsensymmetrie)
  - [ ] Ungerades Signal (Punktsymmetrie)
  - [ ] Zerlegung in geraden und ungeraden Anteil

### 1.2 Elementare Signale
- [ ] Dirac-Impuls $\delta(t)$ und seine Eigenschaften
- [ ] Sprungfunktion $\sigma(t)$ (Heaviside)
- [ ] Rechteckimpuls und Dreieckimpuls
- [ ] Komplexe Exponentialfunktion $e^{j\omega t}$
- [ ] Si-Funktion / sinc-Funktion

### 1.3 Elementare Operationen auf Signalen
- [ ] Zeitverschiebung $x(t - t_0)$
- [ ] Zeitspiegelung $x(-t)$
- [ ] Zeitskalierung $x(at)$
- [ ] Kombination der Operationen (Reihenfolge)
- [ ] Überlagerung und Multiplikation von Signalen

### 1.4 Signalsynthese und -analyse periodischer Signale
- [ ] Motivation: Zerlegung in Schwingungen
- [ ] Fourierreihe (trigonometrische Form)
  - [ ] Analyse: Koeffizienten $a_n$, $b_n$ berechnen
  - [ ] Synthese: Rekonstruktion aus Koeffizienten
- [ ] Fourierreihe (komplexe / exponentielle Form)
  - [ ] Komplexe Koeffizienten $c_n$
  - [ ] Zusammenhang trigonometrische ↔ komplexe Form
- [ ] Amplituden- und Phasenspektrum
- [ ] Gibbs'sches Phänomen
- [ ] Parseval'sches Theorem (Leistung im Zeit- und Frequenzbereich)

### 1.5 Analog-Digital- und Digital-Analog-Umsetzung
- [ ] Abtastung zeitkontinuierlicher Signale
  - [ ] Ideale Abtastung (Dirac-Kamm)
  - [ ] Abtasttheorem nach Shannon–Nyquist
  - [ ] Aliasing: Entstehung und Vermeidung
- [ ] Rekonstruktion (Interpolation / Tiefpassfilterung)
- [ ] Quantisierung
  - [ ] Gleichförmige Quantisierung
  - [ ] Quantisierungsfehler und Quantisierungsrauschen
  - [ ] Signal-Rausch-Verhältnis (SNR) bei Quantisierung

### 1.6 Systeme – Eigenschaften und Klassifikation
- [ ] Definition System, Ein-/Ausgangsdarstellung
- [ ] Linearität (Superpositionsprinzip)
- [ ] Zeitinvarianz
- [ ] LTI-Systeme (Linear Time-Invariant)
- [ ] Kausalität
- [ ] Stabilität (BIBO-Stabilität)
- [ ] Gedächtnislosigkeit vs. dynamische Systeme

### 1.7 Beschreibung von LTI-Systemen im Zeitbereich
- [ ] Impulsantwort $h(t)$
- [ ] Faltungsintegral $y(t) = x(t) * h(t)$
  - [ ] Definition und Herleitung
  - [ ] Rechenregeln (Kommutativität, Assoziativität, Distributivität)
  - [ ] Grafische Faltung
- [ ] Differentialgleichungen als Systembeschreibung
- [ ] Stufensprungantwort $g(t)$ und Zusammenhang mit $h(t)$

---

## Block 2 · Wahrscheinlichkeitsrechnung

### 2.1 Einführung und Grundbegriffe
- [ ] Zufallsexperiment, Ergebnisraum $\Omega$, Ereignis
- [ ] Axiome nach Kolmogorov
- [ ] Laplace-Experiment (Gleichwahrscheinlichkeit)
- [ ] Bedingte Wahrscheinlichkeit $P(A|B)$
- [ ] Multiplikationssatz
- [ ] Stochastische Unabhängigkeit
- [ ] Totale Wahrscheinlichkeit und Bayes'sches Theorem

### 2.2 Mehrstufige Zufallsexperimente
- [ ] Baumdiagramme und Produkträume
- [ ] Kombinatorik (Permutationen, Kombinationen)
  - [ ] Mit / ohne Zurücklegen
  - [ ] Mit / ohne Reihenfolge
- [ ] Binomialkoeffizient und Anwendungen

### 2.3 Diskrete Zufallsvariablen
- [ ] Definition Zufallsvariable und Wahrscheinlichkeitsfunktion
- [ ] Kumulative Verteilungsfunktion (CDF)
- [ ] Wichtige diskrete Verteilungen
  - [ ] Bernoulli-Verteilung
  - [ ] Binomialverteilung
  - [ ] Poisson-Verteilung
  - [ ] Geometrische Verteilung
- [ ] Kenngrößen
  - [ ] Erwartungswert $E[X]$
  - [ ] Varianz $\text{Var}(X)$ und Standardabweichung
  - [ ] Momente und Momentenerzeugende Funktion

### 2.4 Kontinuierliche Zufallsvariablen
- [ ] Wahrscheinlichkeitsdichtefunktion (PDF)
- [ ] Kumulative Verteilungsfunktion (CDF) und Zusammenhang mit PDF
- [ ] Wichtige kontinuierliche Verteilungen
  - [ ] Gleichverteilung (Uniform)
  - [ ] Normalverteilung (Gauß) $\mathcal{N}(\mu, \sigma^2)$
  - [ ] Exponentialverteilung
- [ ] Kenngrößen
  - [ ] Erwartungswert und Varianz
  - [ ] Höhere Momente (Schiefe, Kurtosis)
- [ ] Transformation von Zufallsvariablen

---

## Block 3 · Grundbegriffe der Informationstheorie

### 3.1 Grundlegende Fragestellungen
- [ ] Motivation: Was ist Information?
- [ ] Informationsgehalt eines Ereignisses $I(A) = -\log_2 P(A)$
- [ ] Zusammenhang Wahrscheinlichkeit und Informationsgehalt

### 3.2 Entropiebegriffe
- [ ] Shannon-Entropie $H(X)$
  - [ ] Definition und Einheit (Bit, Nat)
  - [ ] Maximale und minimale Entropie
  - [ ] Entropie der Binärquelle
- [ ] Verbundentropie $H(X, Y)$
- [ ] Bedingte Entropie $H(X|Y)$
- [ ] Transinformation (Mutual Information) $I(X;Y)$
  - [ ] Definition und geometrische Interpretation (Venn-Diagramm)
  - [ ] Symmetrie der Transinformation
- [ ] Kettenregel der Entropie

### 3.3 Anwendungen
- [ ] Quellencodierung
  - [ ] Ziel: Redundanzreduktion
  - [ ] Quellencodierungstheorem (Shannon)
  - [ ] Huffman-Codierung (Prinzip)
- [ ] Kanalkapazität
  - [ ] Binärer symmetrischer Kanal (BSC)
  - [ ] Kanalkapazität $C = \max_{P(X)} I(X;Y)$
  - [ ] Kanalcodierungstheorem (Shannon)

---

## Formelsammlung

- [ ] Elementare Signale und Operationen
- [ ] Fourierreihen-Koeffizienten
- [ ] Faltungsintegral und LTI-Eigenschaften
- [ ] Abtasttheorem
- [ ] Wahrscheinlichkeitsformeln (Bayes, totale W.)
- [ ] Verteilungen (diskret und kontinuierlich)
- [ ] Entropie- und Informationsformeln
