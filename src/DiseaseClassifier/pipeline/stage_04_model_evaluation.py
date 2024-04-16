from DiseaseClassifier.config.configuration import ConfigurationManager
from DiseaseClassifier.components.model_evaluation import Evaluation
from DiseaseClassifier import logger

STAGE_NAME = 'Evaluation Stage'

class EvaluationPipleline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()
    


if __name__ == '__main__':
    try:
        logger.info(f"********************************")
        logger.info(f'>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<')
        obj = EvaluationPipleline()
        obj.main()
        logger.info(f'>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<\n\nX=====================X')

    except Exception as e:
        logger.exception(e)
        raise e