import numpy as np
import pandas as pd

# label_data = pd.read_csv('./_csv/labels/label_data.csv',  encoding='UTF-8')
# label_validation = pd.read_csv('./_csv/labels/label_validation.csv',  encoding='UTF-8')
words = pd.read_csv('./_csv/ksx100.csv', encoding='UTF-8')
y = pd.read_csv('./_csv/y_dic.csv')
val_y = pd.read_csv('./_csv/val_y_dic.csv')


words = np.array(words)

# y = np.array(label_data)
# y = y[:,2]

x = np.load('./_data/x_data_32.npy')
y = np.array(y)

val_x = np.load('./_data/validation_data_32.npy')
val_y = np.array(val_y)

# print(val_y.shape)


y = y.reshape(276886,)
val_y = val_y.reshape(33114,)
# print(x.shape) # (276886, 32, 32, 3)
# print(y.shape) # (276886,)
# print(y[0])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,
    train_size=0.7, shuffle=True, random_state=9) 

# print(x_train.shape) # (193820, 32, 32, 3)
# print(np.unique(x_train))

print(np.unique(y_train))

import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Embedding , LSTM, Input,Conv2D, MaxPool2D, GlobalAveragePooling2D, BatchNormalization, Dropout, ReLU  # Embedding 자연어 쪽에서 많이 씀

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


# model = Sequential()
# model.add(Embedding(input_dim=2350, output_dim=128, input_length=1)) 
# model.add(Dense(2350, activation="softmax"))

from tensorflow.keras.optimizers import Adam
Adam = Adam(learning_rate=0.001)
model.compile(loss='sparse_categorical_crossentropy', optimizer= Adam, metrics=['acc'])

from keras.callbacks import EarlyStopping, ModelCheckpoint
import datetime
date = datetime.datetime.now()
date_time = date.strftime("%m%d_%H%M")

filepath = './_save/'
filename = '.{epoch:04d} - {val_loss:.4f}.hdf5'
modelpath = "".join([filepath, "songulsi", date_time, "-", filename])

es = EarlyStopping(monitor='val_loss',patience=15, mode='auto', verbose=1, restore_best_weights=True,)

mcp = ModelCheckpoint(moniotr='val_loss', mode = 'auto', verobs=1, save_best_only=True, filepath= modelpath)

import time
start_time = time.time()
hist = model.fit(x_train, y_train, epochs=100, validation_data=(val_x, val_y), batch_size=128, callbacks=[es, mcp])  
model.save('./_save/model_save.h5')
end_time = time.time() - start_time


#. 평가, 예측 가즈아!

loss = model.evaluate(x_test,y_test) 

print('걸린시간 : ', end_time)
print('loss : ', loss[0])
print('acc : ', loss[1])
'''

1515/1515 [==============================] - 572s 378ms/step - loss: 0.1214 - acc: 0.9588 - val_loss: 0.5301 - val_acc: 0.8711
Restoring model weights from the end of the best epoch.
Epoch 00033: early stopping
2596/2596 [==============================] - 46s 18ms/step - loss: 0.4138 - acc: 0.8867
걸린시간 :  18908.41751933098
loss :  0.4137674570083618
acc :  0.8867406845092773

'''