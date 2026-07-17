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

Virtuelle Umgebung aktivieren:

```powershell
.venv\Scripts\Activate.ps1
```

Abhängigkeiten installieren:

```powershell
python -m pip install -r requirements.txt
```

## Ausführung

ETL-Pipeline ausführen:

```powershell
python main.py
```

Modell trainieren und speichern:

```powershell
python train.py
```

Gespeichertes Modell für eine Vorhersage verwenden:

```powershell
python predict.py
```

Tests ausführen:

```powershell
python -m unittest discover
```

## Machine Learning

Verwendet wird eine scikit-learn-Pipeline mit:

- `StandardScaler`
- `KNeighborsClassifier`
- `n_neighbors=5`

Das trainierte Modell wird gespeichert unter:

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

## Verwendete Technologien

- Python
- pandas
- scikit-learn
- joblib
- unittest
- Git
- GitHub