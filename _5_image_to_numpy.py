import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from icecream import ic


image_datagen = ImageDataGenerator(rescale=1./255)

#'./test_file/data/train_test_data'
images = image_datagen.flow_from_directory(
    './test_file/validation/data_validation',
    target_size=(32,32),
    batch_size=276886, # [1., 0., 1., 0., 1.] y값 276886
    class_mode='categorical',
    shuffle=False 
)
'''
Found 276886 images belonging to 1 classes.
'''
'''

'''
# np.save('./_data/x_data.npy', arr=images[0][0])
np.save('./_data/validation_data.npy', arr=images[0][0])
exit()



x_train, y_train = images.next()

print(x_train[0].shape)

import matplotlib.pyplot as plt
plt.imshow(x_train[25])
plt.show()