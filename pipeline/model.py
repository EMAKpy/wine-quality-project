class WineRecord:
    """Repräsentiert einen gültigen Wein-Datensatz."""

    def __init__(self, features: dict, quality: int, is_good: int):
        self.features = features
        self.quality = quality
        self.is_good = is_good

    def to_dict(self) -> dict:
        """Gibt alle Daten als Dictionary zurück."""
        return {
            **self.features,
            "quality": self.quality,
            "is_good": self.is_good,
        }

    def __repr__(self) -> str:
        return (
            f"WineRecord(quality={self.quality}, "
            f"is_good={self.is_good})"
        )
    
class PipelineReport:
    """Speichert die Ergebnisse eines Pipeline-Durchlaufs."""

    def __init__(self):
        self.total_rows = 0
        self.valid_rows = 0
        self.invalid_rows = 0

    def mark_valid(self) -> None:
        """Zählt eine gültige Zeile."""
        self.total_rows += 1
        self.valid_rows += 1

    def mark_invalid(self) -> None:
        """Zählt eine ungültige Zeile."""
        self.total_rows += 1
        self.invalid_rows += 1

    def __repr__(self) -> str:
        return (
            f"PipelineReport(total={self.total_rows}, "
            f"valid={self.valid_rows}, "
            f"invalid={self.invalid_rows})"
        )