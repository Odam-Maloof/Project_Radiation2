import tensorflow as tf
from tensorflow import keras
import numpy as np

class PlantIdentifier:
    def __init__(self, model_path, labels):
        self.model = keras.models.load_model(model_path)
        self.labels = labels
        print()

    def predict_plant_species(self, image_path):
        img = keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array1 = np.expand_dims(img_array, axis=0)
        img_array2 = img_array1 / 255.0  # rescale the pixel values to the range [0, 1]
        predictions = self.model.predict(img_array2)
        print(predictions)
        if predictions[predictions == 1].size == 1:
            predicted_index = np.argmax(predictions)
            predicted_plant = self.labels[predicted_index]
        else:
            print("Model is unsure")
            predicted_plant = "undecided"
            num_1 = predictions[0, 0]
            num_2 = predictions[0, 1]
            num_3 = predictions[0, 2]
            num_4 = predictions[0, 3]
            percentage_1 = np.round(num_1 * 100, 2)
            print(percentage_1)
            percentage_2 = np.round(num_2 * 100, 2)
            print(percentage_2)
            percentage_3 = np.round(num_3 * 100, 2)
            print(percentage_3)
            percentage_4 = np.round(num_4 * 100, 2)
            print(percentage_4)
            '''
            print("There are elements in the array that are equal to 1")
            print("There are no elements in the array that are equal to 1")
            '''
        '''predicted_index = np.argmax(predictions)'''
        '''print("This is the predicted index", predicted_index)'''
        '''predicted_plant = self.labels[predicted_index]'''
        '''print("This is the predicted plant", predicted_plant)'''
        return predicted_plant