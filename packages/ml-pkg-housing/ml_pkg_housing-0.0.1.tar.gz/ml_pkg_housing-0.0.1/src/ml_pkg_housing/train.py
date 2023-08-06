import argparse
import logging
import os
import pickle  # noqa

import numpy as np
import pandas as pd
from scipy.stats import randint
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.tree import DecisionTreeRegressor

parser = argparse.ArgumentParser(description="train and save  the model")
parser.add_argument(
    "data_path", type=str, help="Input Data Path", nargs="?", default="data/processed/"
)
parser.add_argument(
    "model_path", type=str, help="Output Model Path", nargs="?", default="artifacts/"
)

args = parser.parse_args()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s : %(name)s : %(message)s")
file_handler = logging.FileHandler(os.path.join("logs/", "trainlog.txt"))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def model_training(housing_prepared, housing_labels):
    """
    The func trains the datasets using various sklearn models like LinearRegression,
    RandomForestRegressor,DecisionTreeRegressor, GridSearchCV, RandomizedSearchCV
    Returns
    -------
    Fitted estimator.
    """
    lin_reg = LinearRegression()

    lin_reg.fit(housing_prepared, housing_labels.values.ravel())

    housing_predictions = lin_reg.predict(housing_prepared)
    lin_mse = mean_squared_error(housing_labels.values.ravel(), housing_predictions)
    lin_rmse = np.sqrt(lin_mse)
    logger.debug("LInear Regression RMSE Value : {}".format(lin_rmse))

    lin_mae = mean_absolute_error(housing_labels.values.ravel(), housing_predictions)
    logger.debug("LInear Regression MAE Value : {}".format(lin_mae))
    tree_reg = DecisionTreeRegressor(random_state=42)
    tree_reg.fit(housing_prepared, housing_labels.values.ravel())

    housing_predictions = tree_reg.predict(housing_prepared)
    tree_mse = mean_squared_error(housing_labels.values.ravel(), housing_predictions)
    tree_rmse = np.sqrt(tree_mse)
    logger.debug("Decision Tree Regression RMSE Value : {}".format(tree_rmse))

    param_distribs = {
        "n_estimators": randint(low=1, high=200),
        "max_features": randint(low=1, high=8),
    }

    forest_reg = RandomForestRegressor(random_state=42)
    rnd_search = RandomizedSearchCV(
        forest_reg,
        param_distributions=param_distribs,
        n_iter=10,
        cv=5,
        scoring="neg_mean_squared_error",
        random_state=42,
    )
    rnd_search.fit(housing_prepared, housing_labels.values.ravel())
    cvres = rnd_search.cv_results_
    for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
        logger.debug(np.sqrt(-mean_score), params)

    param_grid = [
        # try 12 (3×4) combinations of hyperparameters
        {"n_estimators": [3, 10, 30], "max_features": [2, 4, 6, 8]},
        # then try 6 (2×3) combinations with bootstrap set as False
        {"bootstrap": [False], "n_estimators": [3, 10], "max_features": [2, 3, 4]},
    ]

    forest_reg = RandomForestRegressor(random_state=42)
    # train across 5 folds, that's a total of (12+6)*5=90 rounds of training
    grid_search = GridSearchCV(
        forest_reg,
        param_grid,
        cv=5,
        scoring="neg_mean_squared_error",
        return_train_score=True,
    )
    grid_search.fit(housing_prepared, housing_labels.values.ravel())

    grid_search.best_params_
    cvres = grid_search.cv_results_
    for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
        logger.debug(np.sqrt(-mean_score), params)

    feature_importances = grid_search.best_estimator_.feature_importances_
    sorted(zip(feature_importances, housing_prepared.columns), reverse=True)

    final_model = grid_search.best_estimator_

    return lin_reg, tree_reg, final_model


housing_prepared = pd.read_csv(os.path.join(args.data_path, "housing_prepared.csv"))
housing_labels = pd.read_csv(os.path.join(args.data_path, "housing_labels.csv"))

lin_reg_model, tree_reg_model, final_model = model_training(
    housing_prepared, housing_labels
)


pickle.dump(
    lin_reg_model, open(os.path.join(args.model_path, "lin_reg_model.pkl"), "wb")
)

pickle.dump(
    tree_reg_model, open(os.path.join(args.model_path, "tree_reg_model.pkl"), "wb")
)

pickle.dump(final_model, open(os.path.join(args.model_path, "final_model.pkl"), "wb"))
