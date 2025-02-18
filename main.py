from potClassifier import logger
from potClassifier.pipeline.stage_01_data_ingestion import dataingestiontrainingpipeline


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