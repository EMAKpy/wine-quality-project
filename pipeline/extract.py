import csv
from pathlib import Path
from typing import Iterator


def stream_rows(file_path: str | Path) -> Iterator[tuple[int, dict]]:
    """Liest eine CSV-Datei zeilenweise und gibt Zeilennummer und Inhalt zurück."""

    with open(file_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        for line_number, row in enumerate(reader, start=2):
            yield line_number, row