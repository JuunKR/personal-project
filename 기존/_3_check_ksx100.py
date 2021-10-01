import numpy as np
import pandas as pd
from tqdm import tqdm

words = pd.read_csv('./_csv/ksx100.csv', encoding='UTF-8')
label_data = pd.read_csv('./_csv/labels/label_data.csv',  encoding='UTF-8')
label_validation = pd.read_csv('./_csv/labels/label_validation.csv',  encoding='UTF-8')

words = np.array(words)
label_data = np.array(label_data)
label_validation = np.array(label_validation)

# print(type(words)) # <class 'numpy.ndarray'>
# print(words.shape) # (2350, 1)
# print(type(label_data)) # <class 'numpy.ndarray'>
# print(label_data.shape) # (276886, 3)

words = words.reshape(2350,)

delete_words = " ".join(words.tolist())

print(label_validation.shape) # (33114, 3)
temp = []
for index, word in enumerate(label_validation[:,2]):
    if word in delete_words:
        temp.append(label_validation[index,:])
        


ksx100_data = np.array(temp)
print(ksx100_data.shape) # (33114, 3)

pd.DataFrame(ksx100_data).to_csv('./_csv/labels/ksx100_label_validation.csv', header=['path','File_Name','word'], index=None)






# print(label_data[:,2])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# temp = []
# for index, word in enumerate(label_data[:,2]):
#     if word in delete_words:
#         temp.append(label_data[index,:])
        


# ksx100_data = np.array(temp)
# print(ksx100_data.shape) # (276886, 3)

# pd.DataFrame(ksx100_data).to_csv('./_csv/labels/ksx100_label_data.csv', header=['path','File_Name','word'], index=None)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print(label_validation.shape) # (33114, 3)
temp = []
for index, word in enumerate(label_validation[:,2]):
    if word in delete_words:
        temp.append(label_validation[index,:])
        


ksx100_data = np.array(temp)
print(ksx100_data.shape) # (33114, 3)

pd.DataFrame(ksx100_data).to_csv('./_csv/labels/ksx100_label_validation.csv', header=['path','File_Name','word'], index=None)