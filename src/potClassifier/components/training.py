from pathlib import Path
import tensorflow as tf
tf.compat.v1.experimental.output_all_intermediates(True)  # Allows intermediate output
tf.config.run_functions_eagerly(True)  # Enables eager execution
from potClassifier.entity.config_entity import TrainingConfig



class Training :
    def __init__(self,config:TrainingConfig):
        self.config = config
    
    def get_base_model(self) :
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

        # Recompile the model with the same optimizer
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=self.config.params_learning_rate),
            loss="categorical_crossentropy",  # Ensure it matches your class_mode
            metrics=["accuracy"]
    )

    def train_valid_generator(self):
        datagenerator_kwargs = dict(rescale=1/255,
                                     validation_split =0.2
                                     )
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            class_mode = "categorical")

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "validation",
            shuffle = False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation :
            train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else :
            train_data_generator = valid_datagenerator

        
        self.train_generator = train_data_generator.flow_from_directory(
            directory = self.config.training_data,
            subset = "training",
            shuffle = True,
            **dataflow_kwargs)
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def train(self,callback_list: list):
        self.steps_per_epoch = int(self.train_generator.samples // self.train_generator.batch_size)
        self.validation_steps = int(self.valid_generator.samples // self.valid_generator.batch_size)

        print(f"Train Generator Shape: {self.train_generator[0][0].shape}, Labels: {self.train_generator[0][1].shape}")
        print(f"Validation Generator Shape: {self.valid_generator[0][0].shape}, Labels: {self.valid_generator[0][1].shape}")


        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        self.save_model(path = self.config.trained_model_path,model = self.model)


        print("Eager Execution:", tf.executing_eagerly())  # Should print: True
        print("Trainable Variables:", len(self.model.trainable_variables))  # Should be > 0