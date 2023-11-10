import os
from .env_check import obs_copy_folder
from ..utils import constants
def upload_output():
    """
    upload output to openi
    """
    storage_location = os.getenv(constants.STORAGE_LOCATION)
    output_path = str(os.getenv(constants.OUTPUT_PATH))
    job_type = str(os.getenv(constants.JOB_TYPE))

    if storage_location is None or output_path is None:
        raise ValueError(f'Failed to get the environment variable, please make sure the {output_path} and {storage_location} environment variable has been set.')

    if job_type == constants.JOB_TYPE_DEBUG:
        print(f'Debug mode is enabled. output will not be uploaded to openi')
        return output_path
    if job_type == constants.JOB_TYPE_TRAIN:
        print(f'Train mode is enabled. output could be uploaded to openi')
    if storage_location == constants.STORAGE_OBS:
            return upload_output_for_obs()
    return output_path

def upload_output_for_obs():
    cluster = os.getenv(constants.CLUSTER)
    output_path = str(os.getenv(constants.OUTPUT_PATH))
    output_url = str(os.getenv(constants.OUTPUT_URL))
    if output_url is None or output_path is None:
        raise ValueError(f'Failed to obtain environment variables. Please set the {cluster}, {output_path} and {output_url} environment variables.')
    else:
        if not os.path.exists(output_path):
            os.makedirs(output_path) 
    if output_url != "":             
                obs_copy_folder(output_path, output_url)
    return  output_path   
 