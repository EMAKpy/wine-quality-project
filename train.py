from pathlib import Path
from time import perf_counter
import pandas as pd
from sklearn.model_selection import train_test_split
from ml.features import prepare_features
from ml.trainer import (
    build_model,
    evaluate_model,
    save_model,
    train_model,
)


DATA_PATH = Path("data/processed/wine_clean.csv")
MODEL_PATH = Path("models/model.joblib")


def main() -> None:
    """Trainiert, bewertet und speichert das KNN-Modell."""

    start_time = perf_counter()

    print("[1/5] Bereinigte Daten werden geladen ...", flush=True)
    dataframe = pd.read_csv(DATA_PATH)

    print("[2/5] Features und Zielvariable werden vorbereitet ...", flush=True)
    x, y = prepare_features(dataframe)

    print("[3/5] Daten werden in Training und Test aufgeteilt ...", flush=True)
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    print("[4/5] KNN-Modell wird trainiert ...", flush=True)
    model = build_model()
    trained_model = train_model(
        model,
        x_train,
        y_train,
    )

    print("[5/5] Modell wird bewertet und gespeichert ...", flush=True)
    accuracy = evaluate_model(
        trained_model,
        x_test,
        y_test,
    )

    save_model(
        trained_model,
        MODEL_PATH,
    )

    duration = perf_counter() - start_time

    print()
    print("Modelltraining abgeschlossen.")
    print(f"Trainingsdatensätze: {len(x_train)}")
    print(f"Testdatensätze: {len(x_test)}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Modell gespeichert unter: {MODEL_PATH}")
    print(f"Gesamtdauer: {duration:.2f} Sekunden")


if __name__ == "__main__":
    main()