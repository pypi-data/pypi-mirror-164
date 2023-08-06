import argparse
import logging
import os
import pickle

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

parser = argparse.ArgumentParser(description="Scoring of the Models")
parser.add_argument(
    "data_path",
    type=str,
    help="Prepared Test Data Path",
    nargs="?",
    default="data/processed/",
)
parser.add_argument(
    "model_path", type=str, help="Trained Model Path", nargs="?", default="artifacts/"
)
parser.add_argument(
    "output_path",
    type=str,
    help="Model Prediction Output Path",
    nargs="?",
    default="logs/",
)

args = parser.parse_args()


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s : %(name)s : %(message)s")
file_handler = logging.FileHandler(os.path.join(args.output_path, "scores.txt"))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

X_test_prepared = pd.read_csv(os.path.join(args.data_path, "X_test_prepared.csv"))
y_test = pd.read_csv(os.path.join(args.data_path, "y_test.csv"))

final_model = pickle.load(open(os.path.join(args.model_path, "final_model.pkl"), "rb"))


def model_scores():
    """
    The func predicts the median housing value using the best model
    created in train.py and logs the root mean square errors
    Returns
    -------
    None
    """
    final_predictions = final_model.predict(X_test_prepared)
    final_mse = mean_squared_error(y_test, final_predictions)
    final_rmse = np.sqrt(final_mse)
    logger.debug(f"Final RMSE Value is : {final_rmse}")


model_scores()
