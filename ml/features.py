import pandas as pd

FEATURE_COLUMNS = [
    "fixed_acidity",
    "volatile_acidity",
    "citric_acid",
    "residual_sugar",
    "chlorides",
    "free_sulfur_dioxide",
    "total_sulfur_dioxide",
    "density",
    "ph",
    "sulphates",
    "alcohol",
]

TARGET_COLUMN = "is_good"


def prepare_features(
    dataframe: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.Series]:
    """Trennt Eingabemerkmale und Zielvariable."""

    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]

    missing_columns = [
        column
        for column in required_columns
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Fehlende Spalten: {missing_columns}"
        )

    x = dataframe[FEATURE_COLUMNS].copy()
    y = dataframe[TARGET_COLUMN].copy()

    return x, y