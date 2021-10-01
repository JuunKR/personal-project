from tensorflow.keras.preprocessing.image import ImageDataGenerator


train_datagen = ImageDataGenerator(rescale=1./255,
                                 rotation_range = 30,
                                 width_shift_range=0.1,
                                 height_shift_range=0.1,
                                 shear_range=0.2,
                                 zoom_range=0.2,
                                 horizontal_flip=False,
                                 vertical_flip=False,
                                 fill_mode='nearest'
                                 )

train_path = '../data/Training/images/words/train'

xy_train = train_datagen.flow_from_directory(
    train_path,
    batch_size=100,
    target_size=(32,32),
    class_mode='categorical'
)
# Found 221549 images belonging to 2350 classes.



test_path = '../data/Training/images/words/test'

test_datagen = ImageDataGenerator(rescale=1./255)

xy_test = test_datagen.flow_from_directory(
    test_path,
    batch_size=100,
    target_size=(32,32),
    class_mode='categorical'
)
# Found 55337 images belonging to 2350 classes.