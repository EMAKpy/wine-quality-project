# Wine Quality Project

Dieses Miniprojekt verbindet eine ETL-Datenpipeline mit einem Machine-Learning-Modell zur Klassifikation von Rotweinqualität.

## Projektziel

Die Anwendung liest Wein-Rohdaten aus einer CSV-Datei ein, bereinigt und validiert die Datensätze und erstellt eine aufbereitete CSV-Datei.

Anschließend wird ein KNN-Modell trainiert. Das Modell sagt voraus, ob ein Wein als gut eingestuft wird.

Die Zielvariable lautet:

- `0`: Qualität kleiner als 6
- `1`: Qualität mindestens 6

## Datenquelle

Verwendet wird der Red-Wine-Quality-Datensatz des UCI Machine Learning Repository.

Die unveränderten Rohdaten befinden sich unter:

```text
data/raw/winequality-red-original.csv
```

Die Arbeitskopie mit zwei absichtlich ungültigen Zeilen befindet sich unter:

```text
data/raw/winequality-red.csv
```

## Projektstruktur

```text
wine-quality-project/
├── main.py
├── train.py
├── predict.py
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── logs/
├── models/
├── pipeline/
│   ├── __init__.py
│   ├── errors.py
│   ├── extract.py
│   ├── model.py
│   ├── pipeline.py
│   └── transform.py
├── ml/
│   ├── __init__.py
│   ├── features.py
│   └── trainer.py
└── tests/
    ├── __init__.py
    └── test_transform.py
```

## Architektur

Die ETL-Pipeline besteht aus:

1. **Extract:** zeilenweises Lesen der CSV-Datei mit einem Generator
2. **Transform:** Validierung, Typumwandlung und Berechnung von `is_good`
3. **Load:** Speichern gültiger Datensätze in einer neuen CSV-Datei

Ungültige Datensätze werden mit der eigenen Exception `InvalidWineRecordError` behandelt, protokolliert und übersprungen.

## Machine Learning

Verwendet wird eine scikit-learn-Pipeline mit:

- `StandardScaler`
- `KNeighborsClassifier`
- `n_neighbors=5`

Die Daten werden mit `train_test_split` in Trainings- und Testdaten geteilt.

Das trainierte Modell wird mit `joblib` gespeichert unter:

```text
models/model.joblib
```

## Modellergebnis

Die Accuracy auf den Testdaten beträgt:

```text
0.7406
```

Das entspricht:

```text
74,06 %
```

## Installation

Repository herunterladen:

```powershell
git clone DEINE-GITHUB-REPOSITORY-URL
cd wine-quality-project
```

Virtuelle Umgebung erstellen:

```powershell
python -m venv .venv
```

Virtuelle Umgebung unter Windows PowerShell aktivieren:

```powershell
.venv\Scripts\Activate.ps1
```

Abhängigkeiten installieren:

```powershell
python -m pip install -r requirements.txt
```

## Ausführung

### 1. ETL-Pipeline ausführen

```powershell
python main.py
```

Dabei entstehen:

```text
data/processed/wine_clean.csv
logs/invalid_rows.log
```

### 2. Modell trainieren und speichern

```powershell
python train.py
```

Während des Trainings werden die Verarbeitungsschritte angezeigt. Am Ende werden Accuracy, Anzahl der Trainings- und Testdatensätze sowie die Gesamtdauer ausgegeben.

### 3. Interaktive Vorhersage durchführen

```powershell
python predict.py
```

`predict.py` lädt das bereits gespeicherte Modell. Das Modell wird dabei nicht neu trainiert.

Das Programm fragt die elf chemischen Messwerte des Weins einzeln und nacheinander ab:

```text
Feste Säure:
Flüchtige Säure:
Zitronensäure:
Restzucker:
Chloride:
Freies Schwefeldioxid:
Gesamtes Schwefeldioxid:
Dichte:
pH-Wert:
Sulfate:
Alkoholgehalt:
```

Nach jeder Eingabe muss `Enter` gedrückt werden. Dezimalzahlen können mit Punkt oder Komma eingegeben werden.

Anschließend gibt das Programm die vorhergesagte Klasse aus:

```text
Vorhersageklasse: 1
Ergebnis: guter Wein
```

oder:

```text
Vorhersageklasse: 0
Ergebnis: kein guter Wein
```

Wichtig: Das Modell kann nicht anhand eines Wein-Namens, einer Marke oder einer Rebsorte entscheiden. Es benötigt die chemischen Messwerte des Weins.

## Beispielwerte für die interaktive Vorhersage

### Voraussichtlich guter Wein

```text
Feste Säure: 8.0
Flüchtige Säure: 0.35
Zitronensäure: 0.35
Restzucker: 2.0
Chloride: 0.06
Freies Schwefeldioxid: 20
Gesamtes Schwefeldioxid: 45
Dichte: 0.995
pH-Wert: 3.30
Sulfate: 0.75
Alkoholgehalt: 11.5
```

### Voraussichtlich kein guter Wein

```text
Feste Säure: 7.4
Flüchtige Säure: 0.70
Zitronensäure: 0.00
Restzucker: 1.9
Chloride: 0.076
Freies Schwefeldioxid: 11
Gesamtes Schwefeldioxid: 34
Dichte: 0.9978
pH-Wert: 3.51
Sulfate: 0.56
Alkoholgehalt: 9.4
```

Die tatsächliche Vorhersage hängt vom trainierten Modell ab.

## Tests

Alle Unit-Tests ausführen:

```powershell
python -m unittest discover
```

Erwartete Abschlussmeldung:

```text
OK
```

## Fehlerbehandlung

Die eigene Exception `InvalidWineRecordError` wird bei ungültigen Datensätzen ausgelöst.

Die Pipeline fängt diesen erwarteten Fehlertyp ab. Fehlerhafte Zeilen werden protokolliert und übersprungen, ohne den gesamten Pipeline-Lauf abzubrechen.

## Verwendete Technologien

- Python
- pandas
- scikit-learn
- joblib
- unittest
- Git
- GitHub
