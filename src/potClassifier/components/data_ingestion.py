import os
import urllib.request as request
import zipfile
from potClassifier import logger
from potClassifier.utils.common import get_size
from potClassifier.entity.config_entity import dataingestionconfig
from pathlib import Path    


class DataIngestion:
    def __init__(self,config : dataingestionconfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(url=self.config.source_URL,filename =self.config.local_data_file)
            logger.info(f"{filename} download with following info: \n{headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists. Skipping download.")
    def extract_zipfile(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir 

        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(path=unzip_path)
           