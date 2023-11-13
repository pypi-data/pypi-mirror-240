import os
import json
import moxing as mox
import zipfile
import tarfile
from ..utils import constants
def moxing_dataset_to_env(multi_data_url, data_dir, unzip_required):       
        multi_data_json = json.loads(multi_data_url)
        for i in range(len(multi_data_json)):
            path = os.path.join(data_dir, multi_data_json[i]["dataset_name"])
            if not os.path.exists(path):
                os.makedirs(path)
            try:
                if unzip_required == constants.UNZIP_REQUIRED_FALSE:
                    mox.file.copy(multi_data_json[i]["dataset_url"], path)
                    print(f'🎉 Successfully Download {multi_data_json[i]["dataset_url"]} to {path}')
                else:
                    mox.file.copy_parallel(multi_data_json[i]["dataset_url"], path)
                    print(f'🎉 Successfully Download {multi_data_json[i]["dataset_url"]} to {path}')

                if unzip_required == constants.UNZIP_REQUIRED_True:
                    unzip_dataset(path)
            except Exception as e:
                print(f'❌ moxing download {multi_data_json[i]["dataset_url"]} to {path} failed.')

def unzip_dataset(zipfile_path):
    try:
        if zipfile_path.endswith(".tar.gz"):
            with tarfile.open(zipfile_path, 'r:gz') as tar:
                tar.extractall(zipfile_path)
            print(f'🎉 Successfully Extracted {zipfile_path}')
        elif zipfile_path.endswith(".zip"):
            with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
                zip_ref.extractall(zipfile_path)
            print(f'🎉 Successfully Extracted {zipfile_path}')
        else:
            print(f'❌ The dataset is not in tar.gz or zip format!')
    except Exception as e:
        print(f'❌ Extraction failed for {zipfile_path}: {str(e)}')
    finally:
        os.remove(zipfile_path)
        print(f'🎉 Successfully Deleted {zipfile_path}')

def moxing_pretrain_to_env(pretrain_url, pretrain_dir):
    """
    copy pretrain to training image
    """
    pretrain_url_json = json.loads(pretrain_url)  
    for i in range(len(pretrain_url_json)):
        modelfile_path = pretrain_dir + "/" + pretrain_url_json[i]["model_name"]
        try:
            mox.file.copy_parallel(pretrain_url_json[i]["model_url"], modelfile_path) 
            print(f'🎉 Successfully Download {pretrain_url_json[i]["model_url"]} to {modelfile_path}')
        except Exception as e:
            print(f'❌ moxing download {pretrain_url_json[i]["model_url"]} to {modelfile_path} failed.')
    return          

def obs_copy_file(obs_file_url, file_url):
    """
    cope file from obs to obs, or cope file from obs to env, or cope file from env to obs
    """
    try:
        mox.file.copy(obs_file_url, file_url)
        print(f'🎉 Successfully Download {obs_file_url} to {file_url}')
    except Exception as e:
        print(f'❌ moxing download {obs_file_url} to {file_url} failed.')
    return    
    
def obs_copy_folder(folder_dir, obs_folder_url):
    """
    copy folder from obs to obs, or copy folder from obs to env, or copy folder from env to obs
    """
    try:
        mox.file.copy_parallel(folder_dir, obs_folder_url)
        print(f'🎉 Successfully Download {folder_dir} to {obs_folder_url}')
    except Exception as e:
        print(f'❌ moxing download {folder_dir} to {obs_folder_url} failed.')
    return     