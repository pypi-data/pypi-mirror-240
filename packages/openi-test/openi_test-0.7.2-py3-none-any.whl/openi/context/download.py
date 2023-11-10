import os
from .env_check import dataset_to_env, pretrain_to_env, obs_copy_folder
from ..utils import constants

def prepare_dataset():
    storage_location = os.getenv(constants.STORAGE_LOCATION)
    dataset_path = os.getenv(constants.DATASET_PATH)
    if storage_location is None or dataset_path is None:
        raise ValueError(f'Failed to obtain environment variables. Please set the {storage_location} and {dataset_path} environment variables.')
    if os.getenv(storage_location) == constants.STORAGE_OBS:
            return prepare_dataset_for_obs()
    return dataset_path

def prepare_pretrain_model():
    storage_location = os.getenv(constants.STORAGE_LOCATION)
    pretrain_model_path = os.getenv(constants.PRETRAIN_MODEL_PATH)
    if storage_location is None or pretrain_model_path is None:
        raise ValueError(f'Failed to obtain environment variables. Please set the {storage_location} and {pretrain_model_path} environment variables.')
    if storage_location == constants.STORAGE_OBS:
            return prepare_pretrain_model_for_obs()
    return pretrain_model_path

def prepare_output_path():
    storage_location = os.getenv(constants.STORAGE_LOCATION)
    output_path = os.getenv(constants.OUTPUT_PATH)
    if storage_location is None or output_path is None:
            raise ValueError(f'Failed to obtain environment variables. Please set the {constants.STORAGE_LOCATION} and {output_path} environment variables.')
    if storage_location == STORAGE_OBS:
            return prepare_output_path_for_obs()
    return output_path

def prepare_dataset_for_obs():
    cluster = os.getenv(constants.CLUSTER)
    dataset_url = os.getenv(constants.DATASET_URL)
    dataset_path = os.getenv(constants.DATASET_PATH)
    unzip_required = os.getenv(constants.UNZIP_REQUIRED, UNZIP_REQUIRED_FALSE).lower()

    if cluster is None or dataset_url is None or dataset_path is None:
        raise ValueError(f'Failed to obtain environment variables.Please set the {cluster},{dataset_url} and {dataset_path} environment variables')
    else:
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)

    if dataset_url != "":
        dataset_to_env(dataset_url, dataset_path, unzip_required)
    return dataset_path

def prepare_pretrain_model_for_obs():
    pretrain_model_url = os.getenv(constants.PRETRAIN_MODEL_URL)
    pretrain_model_path= os.getenv(constants.PRETRAIN_MODEL_PATH)
    if pretrain_model_url is None or pretrain_model_path is None:
        raise ValueError(f'Failed to obtain environment variables. Please set the {pretrain_model_url} and {pretrain_model_path} environment variables.')
    else:
        if not os.path.exists(pretrain_model_path):
            os.makedirs(pretrain_model_path) 
    if pretrain_model_url != "":             
        pretrain_to_env(pretrain_model_url, pretrain_model_path)
    return pretrain_model_path   

def prepare_output_path_for_obs():	
    output_path = os.getenv(constants.OUTPUT_PATH)	
    if output_path is None:	
        raise ValueError(f'Failed to obtain environment variables. Please set the {output_path} environment variables.')
    else:	
        if not os.path.exists(output_path):	
            os.makedirs(output_path)     
    print(f'please set the output location to {output_path}')
    return output_path 	