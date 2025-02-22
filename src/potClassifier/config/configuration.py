from pathlib import Path
from potClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from potClassifier.utils.common import read_yaml,create_directories,save_json
from potClassifier.entity.config_entity import dataingestionconfig
from potClassifier.entity.config_entity import PrepareBaseModelConfig,PrepareCallbacksConfig,TrainingConfig,EvaluationConfig
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


    def get_training_config(self)-> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir , "PlantVillage")
        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir = Path(training.root_dir),
            trained_model_path= Path(training.trained_model_path),
            updated_base_model_path= Path(prepare_base_model.updated_base_model_path),
            training_data= Path(training_data),
            params_epochs= params.EPOCHS,
            params_batch_size= params.BATCH_SIZE,
            params_is_augmentation= params.AUGMENTATION,
            params_image_size= params.IMAGE_SIZE,
            params_learning_rate = params.LEARNING_RATE
        )
        return training_config
    
    def get_validation_config(self):
        eval_config = EvaluationConfig(
            path_of_model= Path("artifacts/training/model.h5"),
            training_data= Path("artifacts/data_ingestion/PlantVillage"),
            all_params= self.params,
            params_image_size= self.params.IMAGE_SIZE,
            params_batch_size= self.params.BATCH_SIZE
        )
        
        return eval_config 
    




    