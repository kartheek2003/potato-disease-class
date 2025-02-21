from potClassifier.config.configuration import ConfigurationManager
from potClassifier.components.prepare_callbacks import PrepareCallback
from potClassifier.components.training import Training
from potClassifier import logger
from potClassifier.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH



STAGE_NAME = "Training"


class TrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        
        config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config = training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list=callback_list)




if __name__ == "__main__":
    try :
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
    except Exception as e: 
        raise e
