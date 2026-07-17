import unittest

from pipeline.errors import InvalidWineRecordError
from pipeline.transform import parse_float, quality_to_label


class TestTransform(unittest.TestCase):
    """Tests für die reinen Transformationsfunktionen."""

    def test_quality_to_label(self) -> None:
        self.assertEqual(quality_to_label(5), 0)
        self.assertEqual(quality_to_label(6), 1)
        self.assertEqual(quality_to_label(8), 1)

    def test_parse_float_rejects_invalid_number(self) -> None:
        with self.assertRaises(InvalidWineRecordError):
            parse_float("abc", "alcohol")


if __name__ == "__main__":
    unittest.main()