from pathlib import Path

import pandas as pd

from ml.features import FEATURE_COLUMNS
from ml.trainer import load_model


MODEL_PATH = Path("models/model.joblib")


def main() -> None:
    """Lädt das gespeicherte Modell und bewertet einen neuen Wein."""

    model = load_model(MODEL_PATH)

    new_wine = {
        "fixed_acidity": 7.4,
        "volatile_acidity": 0.70,
        "citric_acid": 0.00,
        "residual_sugar": 1.9,
        "chlorides": 0.076,
        "free_sulfur_dioxide": 11.0,
        "total_sulfur_dioxide": 34.0,
        "density": 0.9978,
        "ph": 3.51,
        "sulphates": 0.56,
        "alcohol": 9.4,
    }

    input_data = pd.DataFrame(
        [new_wine],
        columns=FEATURE_COLUMNS,
    )

    prediction = int(model.predict(input_data)[0])

    if prediction == 1:
        result = "guter Wein"
    else:
        result = "kein guter Wein"

    print(f"Vorhersageklasse: {prediction}")
    print(f"Ergebnis: {result}")


if __name__ == "__main__":
    main()