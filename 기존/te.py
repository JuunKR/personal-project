import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Embedding , LSTM, Input,Conv2D, MaxPool2D, GlobalAveragePooling2D, BatchNormalization, ReLU, MaxPooling2D, Dropout  # Embedding 자연어 쪽에서 많이 씀

input1 = Input(shape=(32, 32, 3))
# h = Embedding(input_dim=2350, output_dim=77, input_length=1)(input1)
h = Conv2D(64, 2,padding='same', activation='relu')(input1)
h = MaxPool2D(2, 2)(h)
h = Conv2D(128, 2,padding='same', activation='relu')(h)
h = MaxPool2D(2, 2)(h)
h = Conv2D(128, 2,padding='same', activation='relu')(h)
h = MaxPool2D(2, 2)(h)
h = Conv2D(256, 2,padding='same', activation='relu')(h)
h = MaxPool2D(2, 2)(h)
h = Conv2D(512, 2,padding='same', activation='relu')(h)
h = BatchNormalization()(h)
h = ReLU()(h)
h = Conv2D(512, 2,padding='same', activation='relu')(h)
h = BatchNormalization()(h)
h = ReLU()(h)
h = MaxPool2D(2, 2)(h)
h = GlobalAveragePooling2D()(h)
h = Dropout(0.4)(h)
output1 = Dense(2350, activation='softmax')(h)
model = Model(inputs = input1, outputs = output1)
model.summary()

'''
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_1 (InputLayer)         [(None, 32, 32, 3)]       0
_________________________________________________________________
conv2d (Conv2D)              (None, 32, 32, 64)        832
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 16, 16, 64)        0
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 16, 16, 128)       32896
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 8, 8, 128)         0
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 8, 8, 128)         65664
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 4, 4, 128)         0
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 4, 4, 256)         131328
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 2, 2, 256)         0
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 2, 2, 512)         524800
_________________________________________________________________
batch_normalization (BatchNo (None, 2, 2, 512)         2048
_________________________________________________________________
re_lu (ReLU)                 (None, 2, 2, 512)         0
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 2, 2, 512)         1049088
_________________________________________________________________
batch_normalization_1 (Batch (None, 2, 2, 512)         2048
_________________________________________________________________
re_lu_1 (ReLU)               (None, 2, 2, 512)         0
_________________________________________________________________
max_pooling2d_4 (MaxPooling2 (None, 1, 1, 512)         0
_________________________________________________________________
global_average_pooling2d (Gl (None, 512)               0
_________________________________________________________________
dropout (Dropout)            (None, 512)               0
_________________________________________________________________
dense (Dense)                (None, 2350)              1205550
=================================================================
Total params: 3,014,254
Trainable params: 3,012,206
Non-trainable params: 2,048
_________________________________________________________________
'''