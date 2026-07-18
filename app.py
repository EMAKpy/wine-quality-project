from pathlib import Path

import pandas as pd
import streamlit as st

from ml.features import FEATURE_COLUMNS
from ml.trainer import load_model


MODEL_PATH = Path("models/model.joblib")


st.set_page_config(
    page_title="Wine Quality Predictor",
    page_icon="🍷",
    layout="centered",
)


@st.cache_resource
def get_model():
    """Lädt das gespeicherte Modell einmalig."""

    return load_model(MODEL_PATH)


def create_input_dataframe(wine_data: dict[str, float]) -> pd.DataFrame:
    """Erstellt aus den Eingaben einen DataFrame in korrekter Reihenfolge."""

    return pd.DataFrame(
        [wine_data],
        columns=FEATURE_COLUMNS,
    )


def main() -> None:
    st.title("Wine Quality Predictor")

    st.write(
        "Gib die chemischen Messwerte eines Rotweins ein. "
        "Das Modell schätzt anschließend, ob die Qualität "
        "mindestens 6 beträgt."
    )

    try:
        model = get_model()
    except FileNotFoundError:
        st.error(
            "Das gespeicherte Modell wurde nicht gefunden. "
            "Führe zuerst `python train.py` aus."
        )
        st.stop()

    with st.form("wine_prediction_form"):
        st.subheader("Chemische Messwerte")

        fixed_acidity = st.number_input(
            "Feste Säure",
            min_value=0.0,
            value=7.4,
            step=0.1,
        )

        volatile_acidity = st.number_input(
            "Flüchtige Säure",
            min_value=0.0,
            value=0.70,
            step=0.01,
        )

        citric_acid = st.number_input(
            "Zitronensäure",
            min_value=0.0,
            value=0.00,
            step=0.01,
        )

        residual_sugar = st.number_input(
            "Restzucker",
            min_value=0.0,
            value=1.9,
            step=0.1,
        )

        chlorides = st.number_input(
            "Chloride",
            min_value=0.0,
            value=0.076,
            step=0.001,
            format="%.3f",
        )

        free_sulfur_dioxide = st.number_input(
            "Freies Schwefeldioxid",
            min_value=0.0,
            value=11.0,
            step=1.0,
        )

        total_sulfur_dioxide = st.number_input(
            "Gesamtes Schwefeldioxid",
            min_value=0.0,
            value=34.0,
            step=1.0,
        )

        density = st.number_input(
            "Dichte",
            min_value=0.0,
            value=0.9978,
            step=0.0001,
            format="%.4f",
        )

        ph = st.number_input(
            "pH-Wert",
            min_value=0.0,
            value=3.51,
            step=0.01,
        )

        sulphates = st.number_input(
            "Sulfate",
            min_value=0.0,
            value=0.56,
            step=0.01,
        )

        alcohol = st.number_input(
            "Alkoholgehalt",
            min_value=0.0,
            value=9.4,
            step=0.1,
        )

        submitted = st.form_submit_button(
            "Wein bewerten",
            use_container_width=True,
        )

    if submitted:
        wine_data = {
            "fixed_acidity": fixed_acidity,
            "volatile_acidity": volatile_acidity,
            "citric_acid": citric_acid,
            "residual_sugar": residual_sugar,
            "chlorides": chlorides,
            "free_sulfur_dioxide": free_sulfur_dioxide,
            "total_sulfur_dioxide": total_sulfur_dioxide,
            "density": density,
            "ph": ph,
            "sulphates": sulphates,
            "alcohol": alcohol,
        }

        input_data = create_input_dataframe(wine_data)
        prediction = int(model.predict(input_data)[0])

        st.divider()

        if prediction == 1:
            st.success(
                "Vorhersage: guter Wein – Qualitätsklasse mindestens 6."
            )
        else:
            st.warning(
                "Vorhersage: kein guter Wein – Qualitätsklasse unter 6."
            )

        st.write(f"Vorhersageklasse: `{prediction}`")


if __name__ == "__main__":
    main()