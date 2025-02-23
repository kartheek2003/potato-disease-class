import os 
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename
        # self.model = load_model('updated_model.h5')

    def predict(self):
        # model load
        model = load_model(os.path.join("artifacts","training","model.h5"))

        image_name = self.filename
        
        #PIL format 
        test_image = image.load_img(image_name,target_size = (224,224))

        #pil to np array

        test_image = image.img_to_array(test_image)

        # expand dimensions
        test_image = np.expand_dims(test_image, axis=0)

        # predict

        result = np.argmax(model.predict(test_image),axis=1)

        print(result)

        if result[0] == 1 :
            prediction = "healthy"
            return [{ "image" : prediction}]
        else :
            prediction = "early_blight"
            return [{ "image" : prediction}]

