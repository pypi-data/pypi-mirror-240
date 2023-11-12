from pandas import DataFrame, read_csv
import onnx
from typing import Any
from os.path import join
from os.path import exists
from os import makedirs
from skl2onnx.common.data_types import FloatTensorType
from onnxmltools.convert import convert_xgboost
from random import choice
from string import ascii_uppercase, digits
from datetime import datetime
from darts.timeseries import TimeSeries
from darts.models.forecasting.xgboost import XGBModel
from xgboost import XGBRegressor
from pandas import to_datetime
from pickle import load as pickle_load
from onnx import load as onnx_load

def save_model(
    workdir: str, n_features: int, trained_model: Any, model_index: int
) -> str:
    """Save ONNX model

    Args:
        workdir (str): Working directory
        trained_model (_type_): Trained model

    Return:
        dict: saved model format
    """
    model_type = type(trained_model)
    model_output_path = join(workdir, f"{model_type.__name__}_model_{model_index}")
    if model_type in [XGBModel, XGBRegressor]:
        try:
            initial_type = [("float_input", FloatTensorType([None, n_features]))]
            onx = convert_xgboost(trained_model, initial_types=initial_type)
            with open(model_output_path + ".onnx", "wb") as f:
                f.write(onx.SerializeToString())
            model_fmt = "onnx"
        except ValueError:
            trained_model.save(model_output_path + ".pkl")
            model_fmt = "pkl"
    else:
        raise Exception(f"Model type {model_type} is not supported yet ...")
    
    return {"model_type": str(model_type), "model_fmt": model_fmt, "model_path": f"{model_output_path}.{model_fmt}"}


def save_training_test_data(
        workdir: str, 
        training_data: DataFrame or TimeSeries or None, 
        test_data: DataFrame or TimeSeries or None) -> dict:
    """Saving training and test data

    Args:
        workdir (str): Working directory
        training_data (DataFrame): Training data
        test_data (DataFrame): Test data
    """

    if type(training_data) == TimeSeries:
        training_data = training_data.pd_dataframe()

    if type(test_data) == TimeSeries:
        test_data = test_data.pd_dataframe()
    
    if training_data is not None:
        training_data_path = join(workdir, "training_data.gzip")
        training_data.to_parquet(training_data_path, compression="gzip")
    else:
        training_data_path = None

    if test_data is not None:
        test_data_path = join(workdir, "training_data.gzip")
        test_data.to_parquet(test_data_path, compression="gzip")
    else:
        test_data_path = None

    return {"training_data_path": training_data_path, "test_data_path": test_data_path}


def create_model_log(export_location: str, project_name: str, run_id: str, model_info: list, data_info: dict, user: str, prod: bool):
    """Create modelling log

    Args:
        export_location (str): Base location to save log
        proc_dir (str): processing directory for model
        user (str): User name
        prod (bool): If it's a production run
    """
    output_type = "prod" if prod else "dev"

    model_log_path = join(export_location, "model.csv")

    cur_datetime = datetime.utcnow().strftime('%Y%m%dT%H%M')

    if not exists(model_log_path):
        model_log = {
            "project_name": [],
            "version": [],
            "datetime": [],
            "user": [],
            "type": [],
            "fmt": [],
            "output": [],
            "output_type": [],
            "training_data": [],
            "test_data": []

        }
    else:
        model_log = read_csv(model_log_path)
        model_log = model_log.to_dict("list")

    for proc_model_info in model_info:
        model_log["project_name"].append(project_name)
        model_log["version"].append(run_id)
        model_log["datetime"].append(cur_datetime)
        model_log["user"].append(user)
        model_log["type"].append(proc_model_info["model_type"])
        model_log["fmt"].append(proc_model_info["model_fmt"])
        model_log["output"].append(proc_model_info["model_path"])
        model_log["output_type"].append(output_type)
        model_log["training_data"].append(data_info["training_data_path"])
        model_log["test_data"].append(data_info["test_data_path"])

    df = DataFrame(model_log)
    df.to_csv(model_log_path, index=False)


def import_model(model_version: str, export_location: str = "/DSC/digital_twin/exported_models") -> list:
    """Import saved models

    Args:
        model_version (str): model version to use
        export_location (str, optional): Base directory. Defaults to "/DSC/digital_twin/exported_models".

    Returns:
        list: returned models
    """

    model_log_path = join(export_location, "model.csv")
    model_log = read_csv(model_log_path)
    proc_models = model_log[model_log["version"] == model_version]

    models = []
    for i in range(len(proc_models)):
        proc_model = proc_models.iloc[i]
        
        if proc_model["fmt"] == "pkl":
            with open(proc_model["output"], "rb") as f:
                model = pickle_load(f)
        elif proc_model["fmt"] == "onnx":
            model = onnx_load(proc_model["output"])
        models.append(model)
    return models




def view_model(export_location: str = "/DSC/digital_twin/exported_models", 
               keys: list or None = None,
               filters: dict = {
                    "project_name": None,
                    "datetime_start": None,
                    "datetime_end": None, 
                    "user": None,
                    "fmt": None,
                    "output_type": None,
                }):
    """View recorded modelling information

    Args:
        export_location (str): Base location
        filters = {
            "project_name": ["proj1", "proj2"],
            "datetime_start": 20231112T0249
            "datetime_end": 20231112T0230 
            "user": ["user1", "user2", "user3"],
            "fmt": ["pkl", "onnx"],
            "output_type": ["dev", "prod"],
        }
    """
    model_log_path = join(export_location, "model.csv")
    model_log = read_csv(model_log_path)
    model_log["datetime"] = to_datetime(model_log["datetime"] , format="%Y%m%dT%H%M")

    for filter_key in filters:
        if filters[filter_key] is not None:
            if filter_key == "datetime_start":
                model_log = model_log[model_log["datetime"] >= datetime.strptime(filters["datetime_start"], "%Y%m%dT%H%M")]
            elif filter_key == "datetime_end":
                model_log = model_log[model_log["datetime"] <= datetime.strptime(filters["datetime_end"], "%Y%m%dT%H%M")]
            else:
                model_log = model_log[model_log[filter_key].isin(filters[filter_key])]

    if keys is None:
        print(model_log.to_string())
    else:
        print(model_log[keys].to_string())
    
    print(f"The column names can be shown {list(model_log.columns)}")


def get_run_id(length: int = 6):
    characters = ascii_uppercase + digits
    random_string = ''.join(choice(characters) for _ in range(length))
    return random_string

def export_model(
        project_name: str,
        user: str, 
        trained_models: Any, 
        training_data: DataFrame or TimeSeries, 
        test_data: DataFrame or None, 
        export_location: str = "/DSC/digital_twin/exported_models", 
        prod: bool = False):
    """Export DT model to a standard format

    Args:
        trained_models (Any): Trained model (can be a list)
        training_data (DataFrame): Training data used in the model
        test_data (DataFrame): Test data used in the model
        user (str): the poeple submitted this job
        export_location (str, Default: /DSC/digital_twin/exported_models): Export location
        prod (bool, Default: False): if it is a Production run
    """
    if training_data is None:
        raise Exception("Training data must be specified "
                        "(support types: [darts.timeseries.TimeSeries, pandas.DataFrame])")


    run_id = get_run_id()
    proc_dir = "dev"
    if prod:
        proc_dir = "prod"
    proc_dir = join(export_location, proc_dir, user, run_id)

    if not exists(proc_dir):
        makedirs(proc_dir)

    if not isinstance(trained_models, list):
        trained_models = [trained_models]

    model_info = []
    for model_index, trained_model in enumerate(trained_models):
        model_info.append(save_model(
            proc_dir, len(training_data.columns), trained_model, model_index
        ))

    data_info = save_training_test_data(proc_dir, training_data, test_data)

    create_model_log(export_location, project_name, run_id, model_info, data_info, user, prod)
    