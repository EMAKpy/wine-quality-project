# Wine Quality Project

Dieses Miniprojekt verbindet eine ETL-Datenpipeline mit einem Machine-Learning-Modell.

Die Anwendung liest Rohdaten über Rotwein ein, prüft und bereinigt die Datensätze, erzeugt eine aufbereitete CSV-Datei und trainiert anschließend ein KNN-Klassifikationsmodell.

Das Modell sagt voraus, ob ein Wein als gut eingestuft wird.

## Zielvariable

Die ursprüngliche Qualitätsbewertung liegt als Zahl vor.

Für die Klassifikation wird daraus die Zielvariable `is_good` erstellt:

- `0`: Qualität kleiner als 6
- `1`: Qualität mindestens 6

## Datenquelle

Verwendet wird der Red-Wine-Quality-Datensatz aus dem UCI Machine Learning Repository.

Die Rohdaten befinden sich in:

```text
data/raw/winequality-red.csv