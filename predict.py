from pathlib import Path

import pandas as pd

from ml.features import FEATURE_COLUMNS
from ml.trainer import load_model


MODEL_PATH = Path("models/model.joblib")


def read_float(label: str) -> float:
    """Fragt so lange nach, bis eine gültige Zahl eingegeben wurde."""

    while True:
        user_input = input(f"{label}: ").strip()
        user_input = user_input.replace(",", ".")

        try:
            value = float(user_input)
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue

        if value < 0:
            print("Der Wert darf nicht negativ sein.")
            continue

        return value


def read_wine_data() -> dict[str, float]:
    """Fragt alle Weinwerte einzeln und nacheinander ab."""

    print("Bitte gib die chemischen Messwerte des Weins ein.")
    print()

    wine_data = {
        "fixed_acidity": read_float("Feste Säure"),
        "volatile_acidity": read_float("Flüchtige Säure"),
        "citric_acid": read_float("Zitronensäure"),
        "residual_sugar": read_float("Restzucker"),
        "chlorides": read_float("Chloride"),
        "free_sulfur_dioxide": read_float(
            "Freies Schwefeldioxid"
        ),
        "total_sulfur_dioxide": read_float(
            "Gesamtes Schwefeldioxid"
        ),
        "density": read_float("Dichte"),
        "ph": read_float("pH-Wert"),
        "sulphates": read_float("Sulfate"),
        "alcohol": read_float("Alkoholgehalt"),
    }

    return wine_data


def main() -> None:
    """Lädt das Modell und bewertet die eingegebenen Weinwerte."""

    model = load_model(MODEL_PATH)

    wine_data = read_wine_data()

    input_data = pd.DataFrame(
        [wine_data],
        columns=FEATURE_COLUMNS,
    )

    prediction = int(model.predict(input_data)[0])

    print()
    print(f"Vorhersageklasse: {prediction}")

    if prediction == 1:
        print("Ergebnis: guter Wein")
    else:
        print("Ergebnis: kein guter Wein")


if __name__ == "__main__":
    main()