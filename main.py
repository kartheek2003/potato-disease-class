from potClassifier import logger
from potClassifier.pipeline.stage_01_data_ingestion import dataingestiontrainingpipeline
from potClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTraining
from potClassifier.pipeline.stage_03_training import TrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>stage {STAGE_NAME} started<<<<<<")
        obj = dataingestiontrainingpipeline()
        obj.main()
        logger.info(f">>>>>>stage {STAGE_NAME} completed<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME = "prepare  base model"
if __name__ == "__main__":  
    try:
        logger.info(">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTraining()
        obj.main()
        logger.info(">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
    except Exception as e:
        raise



STAGE_NAME = "Training"


if __name__ == "__main__":
    try :
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
    except Exception as e: 
        raise e

