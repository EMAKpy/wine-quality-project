from pathlib import Path

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

    dataframe = pd.read_csv(DATA_PATH)
    x, y = prepare_features(dataframe)

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = build_model()
    trained_model = train_model(model, x_train, y_train)

    accuracy = evaluate_model(
        trained_model,
        x_test,
        y_test,
    )

    save_model(
        trained_model,
        MODEL_PATH,
    )

    print("Modelltraining abgeschlossen.")
    print(f"Trainingsdatensätze: {len(x_train)}")
    print(f"Testdatensätze: {len(x_test)}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Modell gespeichert unter: {MODEL_PATH}")


if __name__ == "__main__":
    main()