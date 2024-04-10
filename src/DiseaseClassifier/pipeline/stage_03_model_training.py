from DiseaseClassifier.config.configuration import ConfigurationManager
from DiseaseClassifier.components.model_training import Training
from DiseaseClassifier import logger
import tensorflow as tf

STAGE_NAME = 'Training'


class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        early_stopping = tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            min_delta=0,
            patience=0,
            verbose=0,
            mode='auto',
            baseline=None,
            restore_best_weights=False,
            start_from_epoch=0
        )
        callback_list = [early_stopping]
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )



if __name__ == '__main__':
    try:
        logger.info(f"*****************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<')
    except Exception as e :
        logger.exception(e)
        raise e