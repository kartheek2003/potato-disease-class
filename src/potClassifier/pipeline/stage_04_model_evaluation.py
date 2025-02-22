from potClassifier.config.configuration import ConfigurationManager
from potClassifier.components.model_evaluation  import Evaluation
from potClassifier import logger
from potClassifier.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH



STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    
    def main(self):
        config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == '__main__':
    try :
        logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<")
    except Exception as e :
        raise e