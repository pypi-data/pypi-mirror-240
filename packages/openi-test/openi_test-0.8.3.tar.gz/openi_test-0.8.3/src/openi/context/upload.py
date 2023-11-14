import os
from .env_check import upload_folder
from ..utils import constants
def upload_output():
    """
    upload output to openi
    """
    MOXING_REQUIRED = os.getenv(constants.MOXING_REQUIRED)
    output_path = str(os.getenv(constants.OUTPUT_PATH))
    job_type = str(os.getenv(constants.JOB_TYPE))

    if MOXING_REQUIRED is None or output_path is None:
        raise ValueError(f'Failed to get the environment variable, please make sure the {constants.OUTPUT_PATH} and {constants.MOXING_REQUIRED} environment variable has been set.')

    if job_type == constants.JOB_TYPE_DEBUG:
        print(f'Debug mode is enabled. output will not be uploaded to openi')
        return output_path
    if job_type == constants.JOB_TYPE_TRAIN:
        print(f'Train mode is enabled. output could be uploaded to openi')
    if MOXING_REQUIRED == constants.MOXING_REQUIRED_True:
            return upload_output_for_obs()
    return output_path

def upload_output_for_obs():
    output_path = str(os.getenv(constants.OUTPUT_PATH))
    output_url = str(os.getenv(constants.OUTPUT_URL))
    if output_url is None or output_path is None:
        raise ValueError(f'Failed to obtain environment variables. Please set the {constants.OUTPUT_PATH} and {constants.OUTPUT_URL} environment variables.')
    else:
        if not os.path.exists(output_path):
            os.makedirs(output_path) 
    if output_url != "":             
                upload_folder(output_path, output_url)
    return  output_path   
 