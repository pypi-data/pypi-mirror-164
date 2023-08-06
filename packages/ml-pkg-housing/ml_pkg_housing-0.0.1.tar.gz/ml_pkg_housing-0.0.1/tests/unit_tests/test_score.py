import pickle
import sys
import unittest

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

sys.path.append("src/ml_pkg_housing")
import score  # noqa
from score import model_scores  # noqa


class TestModelScores(unittest.TestCase):
    def test_load_housing_data(self):
        with open("artifacts/final_model.pkl", "rb") as f:
            model = pickle.load(f)
            X_test_prepared = pd.read_csv("data/processed/X_test_prepared.csv")
            y_test = pd.read_csv("data/processed/y_test.csv")
            final_predictions = model.predict(X_test_prepared)
            self.assertTrue(len(final_predictions) > 0)
            final_mse = mean_squared_error(y_test, final_predictions)
            final_rmse = np.sqrt(final_mse)
            self.assertTrue((final_mse > 0) and (final_rmse > 0))


if __name__ == "__main__":
    unittest.main()
