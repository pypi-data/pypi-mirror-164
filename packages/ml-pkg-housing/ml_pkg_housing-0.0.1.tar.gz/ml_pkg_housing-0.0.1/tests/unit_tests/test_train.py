import pickle
import sys
import unittest

import pandas as pd

sys.path.append("src/ml_pkg_housing")
import train  # noqa
from train import model_training  # noqa


class TestModelScore(unittest.TestCase):
    def test_model_training(self):
        with self.assertRaises(TypeError):
            model_training()

        with open("artifacts/final_model.pkl", "rb") as f:
            model = pickle.load(f)
            X_test_prepared = pd.read_csv("data/processed/X_test_prepared.csv")
            y_test = pd.read_csv("data/processed/y_test.csv")
            model_ = model.fit(X_test_prepared, y_test.values.ravel())
            self.assertEqual(type(model), type(model_))
            self.assertIs(model_, model)


if __name__ == "__main__":
    unittest.main()
