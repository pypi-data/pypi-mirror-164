import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np
import os.path
import argparse
import mlflow
import mlflow.sklearn
import logging

remote_server_uri = "http://0.0.0.0:5000"  # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)

parser = argparse.ArgumentParser()
parser.add_argument(
    "outdir",
    type=str,
    help="Output dir for data",
    nargs="?",
    default="data/processed/",
)
parser.add_argument(
    "--log-level",
    default=logging.INFO,
    type=lambda x: getattr(logging, x),
    help="Configure the logging level.",
)
parser.add_argument(
    "--no-console",
    default=True,
    type=bool,
    help="Configure the logging console.",
)
parser.add_argument(
    "saveLogs",
    type=str,
    help="Output dir for data",
    nargs="?",
    default="logs/ingest_data.log",
)
p = parser.parse_args()

# import data
housing = pd.read_csv("data/raw/housing.csv")

logger = logging.getLogger(__name__)
logger.setLevel(level=p.log_level)
sh = logging.StreamHandler()
file_handler = logging.FileHandler(p.saveLogs)
logger.addHandler(file_handler)
console = p.no_console
if console:
    logger.addHandler(sh)


def data_prepration(housing):
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
    logger.info(f"Data Prepared")
    return housing_prepared, housing_labels, strat_test_set


housing_prepared, housing_labels, strat_test_set = data_prepration(housing)

housing_prepared.to_csv(
    os.path.join(p.outdir, "housing_prepared.csv"), header=True, index=False
)
housing_labels.to_csv(
    os.path.join(p.outdir, "housing_labels.csv"), header=True, index=False
)
strat_test_set.to_csv(
    os.path.join(p.outdir, "strat_test_set.csv"), header=True, index=False
)

experiment_name = "MLE_TRAINING"
try:
    exp_id = mlflow.create_experiment(name=experiment_name)
except Exception as e:
    exp_id = mlflow.get_experiment_by_name(experiment_name).experiment_id

with mlflow.start_run(experiment_id=exp_id):
    mlflow.log_artifacts(p.outdir)
    mlflow.log_artifact("data/raw/housing.csv")
