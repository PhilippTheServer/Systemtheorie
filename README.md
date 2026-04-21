# LateX Skript Template

# About 

Das Repo verfügt über einen github workflow der on push on `main` automatisch die PDF Version des Skripts generiert und in den Release Bereich hochlädt. Es ist also kein lokales Setup nötig.

---

# Struktur

Der Einstiegspunkt ist die `main.tex`. Dort werden Settings, die Struktur und die Kapitel definiert. Alle Vorlesungen finden sich in `skript/` in der Konvention: `skript/Vorlesung1.text`, `skript/Vorlesung2.tex` etc.

Zusätzliches Wissen wird in `knowledge/<thema>.tex` abgelegt. Dort werden Themen behandelt, die nicht direkt in der Vorlesung vorkommen, aber dennoch relevant sein können, oder einfach interessant sind.

---

# Coding Conventions:

Wichtig: Mathematische ausdrücke werden in Form:
```tex
$$
1 + 1 = 2
$$
```

geschrieben. Es ist wichtig, dass die Zeilenumbrüche vor und nach den Dollarzeichen stehen, damit die Formeln korrekt dargestellt werden.

Inline Mathematische Ausdrücke werden mit einem einzigen Dollarzeichen geschrieben, z.B. `$a + b = c$`.

---

# Skript Aufbau

1. Titelseite
2. Inhaltsverzeichnis
3. Vorlesungen (Kapitelweise)
4. Wissen (Kapitelweise)
5. Formelsammlung

## Code Struktur

```sh
.
├── README.md               # Repo Beschreibung
├── formelsammlung.tex      # Formelsammlung
├── main.tex                # Einstiegspunkt, definiert die Struktur des Skripts
├── preamble.tex            # Alle Pakete und Einstellungen
└── skript                  # Alle Vorlesungen
    └── Vorlesung1.tex
```
