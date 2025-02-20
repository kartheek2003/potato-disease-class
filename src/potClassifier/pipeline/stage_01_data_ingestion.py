from potClassifier.config.configuration import ConfigurationManager
from potClassifier.components.data_ingestion import DataIngestion
from potClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH

from potClassifier import logger

STAGE_NAME = "DATA INGESTION STAGE"

class dataingestiontrainingpipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>stage {STAGE_NAME} started<<<<<<")
        obj = dataingestiontrainingpipeline()
        obj.main()
        logger.info(f">>>>>>stage {STAGE_NAME} completed<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e