from pathlib import Path
from potClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from potClassifier.utils.common import read_yaml,create_directories
from potClassifier.entity.config_entity import dataingestionconfig
from potClassifier.entity.config_entity import PrepareBaseModelConfig,PrepareCallbacksConfig
from potClassifier.constants import *

import os



class ConfigurationManager:
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

    def get_prepare_base_model_configuration(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_directories([config.root_dir])


        preparebasemodelconfig = PrepareBaseModelConfig(root_dir=Path(config.root_dir),
                                                           base_model_path= Path(config.base_model_path),
                                                           updated_base_model_path= Path(config.updated_base_model_path),
                                                           params_image_size=self.params.IMAGE_SIZE,
                                                           params_classes= self.params.CLASSES,
                                                           params_weights=self.params.WEIGHTS,
                                                           params_learning_rate=self.params.LEARNING_RATE,
                                                           params_include_top=self.params.INCLUDE_TOP,
                                                           )
        return preparebasemodelconfig
    
    def get_prepare_callbacks_config(self)->PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([Path(model_ckpt_dir),Path(config.tensorboard_root_log_dir)])
        
        prepare_callbacks_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir= Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )
        return prepare_callbacks_config