from pathlib import Path
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_model() -> Pipeline:
    """Erstellt eine Pipeline aus Skalierung und KNN-Klassifikation."""

    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                KNeighborsClassifier(n_neighbors=5),
            ),
        ]
    )

def train_model(
    model: Pipeline,
    x_train,
    y_train,
) -> Pipeline:
    """Trainiert das Modell mit den Trainingsdaten."""

    model.fit(x_train, y_train)

    return model

def evaluate_model(
    model: Pipeline,
    x_test,
    y_test,
) -> float:
    """Bewertet das trainierte Modell anhand der Testdaten."""

    accuracy = model.score(x_test, y_test)

    return accuracy

def save_model(
    model: Pipeline,
    model_path: str | Path,
) -> None:
    """Speichert das trainierte Modell als Datei."""

    path = Path(model_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, path)

def load_model(
        model_path: str | Path,
) -> Pipeline:
    """Lädt ein gespeichertes Modell aus einer Datei."""

    path = Path(model_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Modell-Datei '{path}' existiert nicht."
        )

    model = joblib.load(path)

    return model
