import csv
from pathlib import Path

from pipeline.errors import InvalidWineRecordError
from pipeline.extract import stream_rows
from pipeline.model import PipelineReport
from pipeline.transform import FEATURE_NAME_MAP, transform_row


OUTPUT_FIELDS = [
    *FEATURE_NAME_MAP.values(),
    "quality",
    "is_good",
]


class WinePipeline:
    """Steuert den vollständigen ETL-Ablauf."""

    def __init__(
        self,
        source_path: str,
        output_path: str,
        error_log_path: str,
    ):
        self.source_path = Path(source_path)
        self.output_path = Path(output_path)
        self.error_log_path = Path(error_log_path)
        self.report = PipelineReport()

    def run(self) -> PipelineReport:
        """Liest, transformiert und speichert die Wein-Datensätze."""

        self.report = PipelineReport()

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.error_log_path.parent.mkdir(parents=True, exist_ok=True)

        with open(
            self.output_path,
            mode="w",
            encoding="utf-8",
            newline="",
        ) as output_file, open(
            self.error_log_path,
            mode="w",
            encoding="utf-8",
        ) as log_file:

            writer = csv.DictWriter(
                output_file,
                fieldnames=OUTPUT_FIELDS,
            )
            writer.writeheader()

            for line_number, row in stream_rows(self.source_path):
                try:
                    record = transform_row(row)

                except InvalidWineRecordError as error:
                    self.report.mark_invalid()

                    log_file.write(
                        f"Zeile {line_number}: {error} | "
                        f"Daten: {row}\n"
                    )

                    continue

                writer.writerow(record.to_dict())
                self.report.mark_valid()

        return self.report

    def __repr__(self) -> str:
        return (
            f"WinePipeline(source_path='{self.source_path}', "
            f"output_path='{self.output_path}')"
        )