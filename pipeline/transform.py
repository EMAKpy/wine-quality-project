from pipeline.errors import InvalidWineRecordError
from pipeline.model import WineRecord


def parse_float(value: str, field_name: str) -> float:
    """Wandelt einen Textwert in eine nicht negative Kommazahl um."""

    if value is None or value.strip() == "":
        raise InvalidWineRecordError(
            f"Feld '{field_name}' ist leer."
        )

    try:
        number = float(value.strip())
    except ValueError as error:
        raise InvalidWineRecordError(
            f"Feld '{field_name}' enthält keine gültige Zahl: '{value}'."
        ) from error

    if number < 0:
        raise InvalidWineRecordError(
            f"Feld '{field_name}' darf nicht negativ sein: {number}."
        )

    return number


def parse_quality(value: str) -> int:
    """Wandelt die Qualitätsangabe in eine ganze Zahl von 0 bis 10 um."""

    if value is None or value.strip() == "":
        raise InvalidWineRecordError(
            "Feld 'quality' ist leer."
        )

    try:
        quality = int(value.strip())
    except ValueError as error:
        raise InvalidWineRecordError(
            f"Feld 'quality' enthält keine gültige ganze Zahl: '{value}'."
        ) from error

    if quality < 0 or quality > 10:
        raise InvalidWineRecordError(
            f"Feld 'quality' muss zwischen 0 und 10 liegen: {quality}."
        )

    return quality


def quality_to_label(quality: int) -> int:
    """Wandelt die Qualitätszahl in eine binäre Klasse um."""

    if quality >= 6:
        return 1

    return 0


FEATURE_NAME_MAP = {
    "fixed acidity": "fixed_acidity",
    "volatile acidity": "volatile_acidity",
    "citric acid": "citric_acid",
    "residual sugar": "residual_sugar",
    "chlorides": "chlorides",
    "free sulfur dioxide": "free_sulfur_dioxide",
    "total sulfur dioxide": "total_sulfur_dioxide",
    "density": "density",
    "pH": "ph",
    "sulphates": "sulphates",
    "alcohol": "alcohol",
}


def transform_row(row: dict) -> WineRecord:
    """Validiert eine CSV-Zeile und erstellt einen WineRecord."""

    features = {}

    for source_name, target_name in FEATURE_NAME_MAP.items():
        value = row.get(source_name)
        features[target_name] = parse_float(value, source_name)

    quality = parse_quality(row.get("quality"))
    is_good = quality_to_label(quality)

    return WineRecord(
        features=features,
        quality=quality,
        is_good=is_good,
    )