import argparse
import logging
import os

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split

HOUSING_PATH = os.path.join("./data", "raw")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s : %(name)s : %(message)s")
file_handler = logging.FileHandler(os.path.join("logs/", "trainlog.txt"))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_housing_data(housing_path=HOUSING_PATH):
    """
    Loads Housing Data and return Dataframe
    Returns
    -------
    DataFrame
    """
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def data_preprocessing():
    """
    It split datasets into train and test and preprocess the data and returns the datasets
    Returns
    -------
    Train and Tests DataFtrames
    """
    housing = load_housing_data()

    train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

    housing["income_cat"] = pd.cut(
        housing["median_income"],
        bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
        labels=[1, 2, 3, 4, 5],
    )
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()
    imputer = SimpleImputer(strategy="median")

    housing_num = housing.drop("ocean_proximity", axis=1)

    imputer.fit(housing_num)
    X = imputer.transform(housing_num)
    housing_tr = pd.DataFrame(X, columns=housing_num.columns, index=housing.index)
    housing_tr["rooms_per_household"] = (
        housing_tr["total_rooms"] / housing_tr["households"]
    )
    housing_tr["bedrooms_per_room"] = (
        housing_tr["total_bedrooms"] / housing_tr["total_rooms"]
    )

    housing_tr["population_per_household"] = (
        housing_tr["population"] / housing_tr["households"]
    )
    housing_cat = housing[["ocean_proximity"]]
    housing_prepared = housing_tr.join(pd.get_dummies(housing_cat, drop_first=True))

    logger.info("Data Prepared")

    X_test = strat_test_set.drop("median_house_value", axis=1)
    y_test = strat_test_set["median_house_value"].copy()

    X_test_num = X_test.drop("ocean_proximity", axis=1)
    X_test_prepared = imputer.transform(X_test_num)
    X_test_prepared = pd.DataFrame(
        X_test_prepared, columns=X_test_num.columns, index=X_test.index
    )
    X_test_prepared["rooms_per_household"] = (
        X_test_prepared["total_rooms"] / X_test_prepared["households"]
    )
    X_test_prepared["bedrooms_per_room"] = (
        X_test_prepared["total_bedrooms"] / X_test_prepared["total_rooms"]
    )
    X_test_prepared["population_per_household"] = (
        X_test_prepared["population"] / X_test_prepared["households"]
    )

    X_test_cat = X_test[["ocean_proximity"]]
    X_test_prepared = X_test_prepared.join(pd.get_dummies(X_test_cat, drop_first=True))
    return housing_prepared, housing_labels, strat_test_set, X_test_prepared, y_test


(
    housing_prepared,
    housing_labels,
    strat_test_set,
    X_test_prepared,
    y_test,
) = data_preprocessing()

parser = argparse.ArgumentParser(description="Preprocessing the data")

parser.add_argument(
    "output_path",
    type=str,
    help="Output path for saving datasets",
    nargs="?",
    default="data/processed/",
)
args = parser.parse_args()
housing_prepared.to_csv(
    os.path.join(args.output_path, "housing_prepared.csv"), header=True, index=False
)

housing_labels.to_csv(
    os.path.join(args.output_path, "housing_labels.csv"), header=True, index=False
)

strat_test_set.to_csv(
    os.path.join(args.output_path, "strat_test_set.csv"), header=True, index=False
)

X_test_prepared.to_csv(
    os.path.join(args.output_path, "X_test_prepared.csv"), header=True, index=False
)

y_test.to_csv(os.path.join(args.output_path, "y_test.csv"), header=True, index=False)
