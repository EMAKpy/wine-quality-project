from pipeline.pipeline import WinePipeline


def main() -> None:
    pipeline = WinePipeline(
        source_path="data/raw/winequality-red.csv",
        output_path="data/processed/wine_clean.csv",
        error_log_path="logs/invalid_rows.log",
    )

    report = pipeline.run()

    print("ETL-Pipeline abgeschlossen.")
    print(report)


if __name__ == "__main__":
    main()