import json
import os
import shutil
from unittest import mock

import dill
from botocore.exceptions import NoCredentialsError
import mongomock

from flowi.experiment_tracking.flavors import SklearnFlavor
from flowi.settings import MONGO_ENDPOINT_URL

import flowi.settings
from flowi.__main__ import main

FLOW_CHART = {
    "nodes": {
        "node-load-1": {
            "id": "node-load-1",
            "type": "Load",
            "properties": {
                "name": "LoadFile",
                "function_name": "load_file",
                "class": "LoadLocal",
                "attributes": {
                    "train_path": "iris.csv",
                    "test_path": "",
                    "test_split": 0.2,
                    "file_type": "csv",
                    "target_column": "class",
                },
            },
        },
        "node-load-2": {
            "id": "node-load-2",
            "type": "Load",
            "properties": {
                "name": "LoadFile",
                "function_name": "load_file",
                "class": "LoadLocal",
                "attributes": {"train_path": "iris.csv", "test_path": "", "test_split": 0.2, "file_type": "csv"},
            },
        },
        # "node-label-enc": {
        #     "id": "node-label-enc",
        #     "type": "Label",
        #     "properties": {
        #         "name": "LabelEncoder",
        #         "class": "Label",
        #         "attributes": {"column": "class", "is_target_column": True},
        #     },
        # },
        "node-fillna": {
            "id": "node-fillna",
            "type": "Preprocessing",
            "properties": {
                "name": "Fillna",
                "function_name": "fillna",
                "class": "PreprocessingDataframe",
                "attributes": {
                    "columns": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
                    "exclude_columns": [],
                    "strategy": ["mean", "median"],
                },
            },
        },
        "node-standard-scaler": {
            "id": "node-standard-scaler",
            "type": "Preprocessing",
            "properties": {
                "name": "StandardScaler",
                "function_name": "standard_scaler",
                "class": "PreprocessingDataframe",
                "attributes": {
                    "columns": [],
                    "exclude_columns": ["class"],
                    "with_mean": True,
                    "with_std": True,
                },
            },
        },
        "node-model-svc": {
            "id": "node-model-svc",
            "type": "Models",
            "properties": {
                "name": "SVC",
                "function_name": "svc",
                "class": "Classification",
                "attributes": {'decision_function_shape': 'ovr', 'kernel': 'rbf', 'max_iter': -1, 'C': [12.0], 'coef0': 0.0, 'gamma': 'scale', 'shrinking': True, 'break_ties': False, 'cache_size': 200, 'degree': 3.0, 'probability': False, 'target_column': 'class', 'class_weight': None, 'tol': 0.001}},
        },
        "node-model-svc2": {
            "id": "node-model-svc2",
            "type": "Models",
            "properties": {
                "name": "SVC",
                "function_name": "svc",
                "class": "Classification",
                "attributes": {"target_column": "class"}},
        },
        "node-model-tfcnn": {
            "id": "node-model-tfcnn",
            "type": "Models",
            "properties": {
                "name": "tf_cnn",
                "function_name": "tf_cnn",
                "class": "Classification",
                "attributes": {}},
        },
        "node-metric-accuracy": {
            "id": "node-metric-accuracy",
            "type": "Metrics",
            "properties": {
                "name": "accuracy",
                "function_name": "accuracy",
                "class": "Classification",
                "attributes": {}},
        },
        "node-metric-precision": {
            "id": "node-metric-precision",
            "type": "Metrics",
            "properties": {
                "name": "precision",
                "function_name": "precision",
                "class": "Classification",
                "attributes": {"average": "macro"}
            },
        },
        "node-metric-accuracy3": {
            "id": "node-metric-accuracy3",
            "type": "Metrics",
            "properties": {
                "name": "accuracy",
                "function_name": "accuracy",
                "class": "Classification",
                "attributes": {}
            },
        },
        "node-save": {
            "id": "node-save",
            "type": "Save",
            "properties": {
                "name": "SaveFile",
                "function_name": "save_file",
                "class": "SaveLocal",
                "attributes": {"file_type": "csv", "file_name": "saved.csv", "label_column": "class"},
            },
        },
    },
    "links": {
        "link-load-fillna-1": {"from": {"nodeId": "node-load-1"}, "to": {"nodeId": "node-fillna"}},
        "link-load-fillna-2": {"from": {"nodeId": "node-load-2"}, "to": {"nodeId": "node-fillna"}},
        # "link-label-enc-fillna": {"from": {"nodeId": "node-label-enc"}, "to": {"nodeId": "node-fillna"}},
        "link-label-fillna-standard-scaler": {
            "from": {"nodeId": "node-fillna"},
            "to": {"nodeId": "node-standard-scaler"},
        },
        "link-standard-scaler-svc": {"from": {"nodeId": "node-standard-scaler"}, "to": {"nodeId": "node-model-svc"}},
        "link-standard-scaler-svc2": {"from": {"nodeId": "node-standard-scaler"}, "to": {"nodeId": "node-model-svc2"}},
        "link-standard-scaler-tfcnn": {
            "from": {"nodeId": "node-standard-scaler"},
            "to": {"nodeId": "node-model-tfcnn"},
        },
        "link-svc-accuracy": {"from": {"nodeId": "node-model-svc"}, "to": {"nodeId": "node-metric-accuracy"}},
        "link-svc-precision": {"from": {"nodeId": "node-model-svc2"}, "to": {"nodeId": "node-metric-precision"}},
        "link-svc-accuracy3": {"from": {"nodeId": "node-model-tfcnn"}, "to": {"nodeId": "node-metric-accuracy3"}},
        "link-accuracy-save": {"from": {"nodeId": "node-metric-accuracy"}, "to": {"nodeId": "node-save"}},
        "link-precision-save": {"from": {"nodeId": "node-metric-precision"}, "to": {"nodeId": "node-save"}},
        "link-accuracy3-save": {"from": {"nodeId": "node-metric-accuracy3"}, "to": {"nodeId": "node-save"}},
    },
}


# @mongomock.patch(servers=((MONGO_ENDPOINT_URL, 27017),))
# def test_end_to_end_train(mocker):
#     mocker.patch.object(flowi.settings, "FLOW_NAME", "End2End Test Flow")
#     mocker.patch.object(flowi.settings, "EXPERIMENT_TRACKING", "MLflow")
#     mocker.patch("mlflow.register_model")
#     mocker.patch("flowi.experiment_tracking._mlflow.MlflowClient.transition_model_version_stage")
#
#     try:
#         metric = "accuracy"
#         threshold = "0.8"
#         main(["train", "--metric", metric, "--threshold", threshold, "--chart", json.dumps(FLOW_CHART)])
#     # TODO: Fix airflow write
#     except OSError:
#         pass
#     # TODO: Add boto3 mock
#     except NoCredentialsError:
#         pass
#
#     os.remove("saved.csv")


PREDICT_SOURCE = {
    "id": "node-load-1",
    "type": "Load",
    "properties": {
        "name": "LoadFile",
        "function_name": "load_file",
        "class": "LoadLocal",
        "attributes": {"train_path": "", "test_path": "iris_pred.csv", "test_split": 0.0, "file_type": "csv"},
    },
}

PREDICT_DESTINY = {
    "id": "node-save-1",
    "type": "Save",
    "properties": {
        "name": "SaveFile",
        "function_name": "save_file",
        "class": "SaveLocal",
        "attributes": {"file_type": "csv", "file_name": "saved.csv", "label_column": "class"},
    },
}


def test_end_to_end_predict(mocker):
    mocker.patch.object(flowi.settings, "FLOW_NAME", "End2End Test Flow")
    mocker.patch.object(flowi.settings, "EXPERIMENT_TRACKING", "MLflow")
    mock_model = mock.Mock()
    mock_model.version.return_value = "1"
    mock_model.run_id.return_value = "run_id"
    mocker.patch("flowi.experiment_tracking._mlflow.MlflowClient.get_model_version", mock_model)
    mocker.patch("flowi.experiment_tracking._mlflow.MlflowClient.download_artifacts")

    shutil.copytree("artifacts/classification", ".", dirs_exist_ok=True)

    with open("model.pkl", "rb") as f:
        model = dill.load(f)
    loaded_model = SklearnFlavor(model=model)
    mocker.patch("flowi.prediction.prediction_batch.load_model_by_version",  return_value=loaded_model)

    try:
        main(["predict", "--source", json.dumps(PREDICT_SOURCE), "--destiny", json.dumps(PREDICT_DESTINY)])
        os.remove("saved.csv")
    # TODO: Add mock to airflow write
    except OSError:
        pass

    os.remove("saved.csv")
    shutil.rmtree("columns")
    shutil.rmtree("drift")
    shutil.rmtree("transformers")
    os.remove("model.pkl")
