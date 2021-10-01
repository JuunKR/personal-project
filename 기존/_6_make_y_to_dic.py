import numpy as np
import pandas as pd

label_data = pd.read_csv('./_csv/labels/label_data.csv',  encoding='UTF-8')
label_validation = pd.read_csv('./_csv/labels/label_validation.csv',  encoding='UTF-8')
words = pd.read_csv('./_csv/ksx100.csv', encoding='UTF-8')
words = np.array(words)

words = words.reshape(2350,)
y = np.array(label_data)
y = y[:,2]

val_y = np.array(label_validation)
val_y = val_y[:,2]
# print(y.shape) # (276886,)
# print(y[0])

#. val_y에 쓸거
test = {}
for i, j in enumerate(words):
    test[j] = i 
     

# print(test)

sample = []
for i in val_y:
    sample.append(test[i])

print(sample[:10])

dic = np.array(sample)
# print(type(ksx)) # <class 'numpy.ndarray'>

dic = pd.DataFrame(dic)
dic.to_csv('./_csv/val_y_dic.csv', index=False)

exit()

#. y 에 쓴거
test = {}
for i, j in enumerate(words):
    test[j] = i 
     

# print(test)

sample = []
for i in y:
    sample.append(test[i])

print(sample[:10])

dic = np.array(sample)
# print(type(ksx)) # <class 'numpy.ndarray'>

dic = pd.DataFrame(dic)
dic.to_csv('./_csv/dic.csv', index=False)
