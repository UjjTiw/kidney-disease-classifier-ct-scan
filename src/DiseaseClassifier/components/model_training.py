import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from DiseaseClassifier.config.configuration import TrainingConfig
from pathlib import Path


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_model_path
        )

    
    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split =  0.25
        )

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear'
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            class_mode="categorical",
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.25,
                height_shift_range=0.15,
                shear_range=0.17,
                zoom_range=0.19,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='training',
            shuffle=True,
            class_mode="categorical",
            **dataflow_kwargs
        )
        

    @staticmethod   
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def train(self, callback_list: list):
        self.steps_pre_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs = self.config.params_epoch,
            steps_per_epoch = self.steps_pre_epoch,
            validation_steps = self.validation_steps,
            validation_data = self.valid_generator,
            callbacks = callback_list
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
        