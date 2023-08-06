from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.metrics import mean_squared_error
import pandas as pd
import pickle
import argparse
import mlflow
import mlflow.sklearn
import logging

remote_server_uri = "http://0.0.0.0:5000"  # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)

parser = argparse.ArgumentParser()
parser.add_argument(
    "read_data",
    type=str,
    help="Read data",
    nargs="?",
    default="data/processed/strat_test_set.csv",
)
parser.add_argument(
    "read_model_pickle",
    type=str,
    help="Read Model",
    nargs="?",
    default="artifacts/model.sav",
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
    default="logs/score.log",
)

p = parser.parse_args()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(level=p.log_level)
sh = logging.StreamHandler()
file_handler = logging.FileHandler(p.saveLogs)
logger.addHandler(file_handler)
console = p.no_console
if console:
    logger.addHandler(sh)


def score(strat_test_set, final_model, housing):
    imputer = SimpleImputer(strategy="median")
    housing_num = housing.drop(["median_house_value", "ocean_proximity"], axis=1)
    imputer.fit(housing_num)
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

    final_predictions = final_model.predict(X_test_prepared)
    final_mse = mean_squared_error(y_test, final_predictions)
    final_rmse = np.sqrt(final_mse)
    logger.info(f"Score generated")
    return final_rmse


strat_test_set = pd.read_csv(p.read_data)
housing = pd.read_csv("data/raw/housing.csv")
# load the model
loaded_model = pickle.load(open(p.read_model_pickle, "rb"))
final_rmse = score(strat_test_set, loaded_model, housing)
print(final_rmse)

experiment_name = "MLE_TRAINING"
try:
    exp_id = mlflow.create_experiment(name=experiment_name)
except Exception as e:
    exp_id = mlflow.get_experiment_by_name(experiment_name).experiment_id

with mlflow.start_run(experiment_id=exp_id):
    mlflow.log_metric(key="rmse", value=final_rmse)
