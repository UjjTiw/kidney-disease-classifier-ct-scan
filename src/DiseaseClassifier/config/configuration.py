import os
from DiseaseClassifier.constants import *
from DiseaseClassifier.utils.common import read_yaml, create_directories
from DiseaseClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig,TrainingConfig 

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL = config.source_URL,
            local_data_files = config.local_data_files,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config


    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_classes= self.params.CLASSES,
            params_image_size= self.params.IMAGE_SIZE,
            params_include_top= self.params.INCLUDE_TOP,
            params_weights= self.params.WEIGHTS,
            params_learning_rate= self.params.LEARNING_RATE
        )
        return prepare_base_model_config
    

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone")
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epoch= params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_image_size= params.IMAGE_SIZE,
            params_is_augmentation=params.AUGMENTATION
        )

        return training_config