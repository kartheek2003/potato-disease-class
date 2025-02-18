from potClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from potClassifier.utils.common import read_yaml,create_directories
from potClassifier.entity.config_entity import dataingestionconfig

class configurationmanager:
    def __init__(self, 
                 config_filepath: CONFIG_FILE_PATH,
                 params_filepath: PARAMS_FILE_PATH,
                 ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->dataingestionconfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_inges_config = dataingestionconfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir,
        )
        return data_inges_config