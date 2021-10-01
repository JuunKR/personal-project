import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Embedding , LSTM, Input,Conv2D, MaxPool2D, GlobalAveragePooling2D, BatchNormalization, Dropout, ReLU  # Embedding 
from tensorflow.keras.optimizers import Adam

class Build_Model(object):

    def build_model(self):
        input1 = Input(shape=(32, 32, 3))
        # h = Embedding(input_dim=2350, output_dim=77, input_length=1)(input1)
        h = Conv2D(64, 2,padding='same', activation='relu')(input1)
        h = MaxPool2D(2, 2)(h)
        h = Conv2D(128, 2,padding='same', activation='relu')(h)
        h = MaxPool2D(2, 2)(h)
        h = Conv2D(256, 2,padding='same', activation='relu')(h)
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

        adam = Adam(learning_rate=0.001)
        model.compile(loss='categorical_crossentropy', optimizer= adam, metrics=['acc'])

        return model