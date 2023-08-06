import sys
import unittest

sys.path.append("src/ml_pkg_housing")
import ingest_data  # noqa
from ingest_data import data_preprocessing, load_housing_data  # noqa


class TestUtils(unittest.TestCase):
    def test_load_housing_data(self):
        housing_data = load_housing_data()
        self.assertTrue(len(housing_data) > 0)
        self.assertEqual(len(housing_data), 20640)
        self.assertEqual(len(housing_data.columns), 10)
        print("Data Testing Done")

    def test_data_preprocessing(self):
        data_preprocessed = data_preprocessing()
        housing_prepared = data_preprocessed[0]
        X_test_prepared = data_preprocessed[3]
        strat_test_set = data_preprocessed[2]
        self.assertTrue(len(housing_prepared) > 0)
        self.assertEqual(len(housing_prepared), 20640 * (80 / 100))
        self.assertTrue(len(X_test_prepared) > 0)
        self.assertEqual(len(X_test_prepared), 20640 * (20 / 100))
        self.assertEqual(len(strat_test_set), len(X_test_prepared))
        print("Data Preprocessing Testing Done")


if __name__ == "__main__":
    unittest.main()
