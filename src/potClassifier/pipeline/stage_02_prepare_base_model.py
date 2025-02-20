from potClassifier.config.configuration import ConfigurationManager
from potClassifier.components.prepare_base_model import preparebasemodel
from potClassifier import logger
from potClassifier.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH

STAGE_NAME = "prepare  base model"


class PrepareBaseModelTraining:
    def __init__(self):
        pass
    def main(self) :
        config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)
        preparebasemodelconfig = config.get_prepare_base_model_configuration()
        prep_base_model = preparebasemodel(preparebasemodelconfig)
        prep_base_model.get_base_model()
        prep_base_model.update_base_model()



if __name__ == "__main__":  
    try:
        logger.info(">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTraining()
        obj.main()
        logger.info(">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
    except Exception as e:
        raise
