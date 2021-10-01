from tensorflow.keras.datasets import fashion_mnist
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

image_datagen = ImageDataGenerator(rescale=1./255)

#'./test_file/data/train_test_data'
images = image_datagen.flow_from_directory(
    './test_file/validation/data_validation',
    target_size=(32,32),
    batch_size=276886, # [1., 0., 1., 0., 1.] y값 276886
    class_mode='categorical',
    shuffle=False 
)

