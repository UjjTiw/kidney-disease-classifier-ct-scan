from DiseaseClassifier import logger
from DiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from DiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from DiseaseClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from DiseaseClassifier.pipeline.stage_04_model_evaluation import EvaluationPipleline



STAGE_NAME = "Data Ingestion Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX================X")
except Exception as e:
        raise e

STAGE_NAME = "Prepare base model"
try:
        logger.info(f"****************************")
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        prepare_base_model= PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<< \n\nX==================X")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Trainig the model"
try:
        logger.info(f"****************************")
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        model_trainer = ModelTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<< \n\nX==================X")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = 'Evaluation Stage'
try:
        logger.info(f"********************************")
        logger.info(f'>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<')
        model_evaluation = EvaluationPipleline()
        model_evaluation.main()
        logger.info(f'>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<\n\nX=====================X')
except Exception as e:
        logger.exception(e)
        raise e