from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import numpy as np
import pandas as pd
import pickle
import mlflow
import mlflow.sklearn
import argparse
import logging

remote_server_uri = "http://0.0.0.0:5000"  # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)

parser = argparse.ArgumentParser()

parser.add_argument(
    "read_data",
    type=str,
    help="Read data",
    nargs="?",
    default="data/processed/housing_prepared.csv",
)
parser.add_argument(
    "read_labels",
    type=str,
    help="Read labels",
    nargs="?",
    default="data/processed/housing_labels.csv",
)
parser.add_argument(
    "modelFile",
    type=str,
    help="model file",
    nargs="?",
    default="artifacts/model.sav",
)
parser.add_argument(
    "outdir",
    type=str,
    help="Output dir for model",
    nargs="?",
    default="artifacts/",
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
    default="logs/train.log",
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


def train(housing_prepared, housing_labels):
    param_grid = [
        {"n_estimators": [3, 10, 30], "max_features": [2, 4, 6, 8]},
        {"bootstrap": [False], "n_estimators": [3, 10], "max_features": [2, 3, 4]},
    ]
    forest_reg = RandomForestRegressor(random_state=42)
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
        print(np.sqrt(-mean_score), params)

    final_model = grid_search.best_estimator_
    logger.info(f"Model created")
    logger.debug(f"Model not created")
    return final_model


housing_prepared = pd.read_csv(p.read_data)
housing_labels = pd.read_csv(p.read_labels)

model = train(housing_prepared, housing_labels)
# save the model
pickle.dump(model, open(p.modelFile, "wb"))

experiment_name = "MLE_TRAINING"
try:
    exp_id = mlflow.create_experiment(name=experiment_name)
except Exception as e:
    exp_id = mlflow.get_experiment_by_name(experiment_name).experiment_id

with mlflow.start_run():
    mlflow.log_artifacts(p.outdir)
