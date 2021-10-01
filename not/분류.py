import pandas as pd
import glob
import shutil as sh
import os

def separate_train_images(path, data):
    
    words = pd.read_csv('csv/ksx100.csv', encoding='UTF-8')
    ksx1001 = words['0'].values.tolist()
    # # 분류를 위한 폴더 만들기
    for ksx in ksx1001:
        os.makedirs(path + '/' + ksx)
    
    # 파일 분류
    for ksx in ksx1001:
        f_name = []
        for index, word in enumerate(data['word']):
            if word == ksx :
                f_name.append(str(data['img_name'][index]))
        for name in f_name:
            sh.move(path + '/' + name, path + '/' + ksx)
                
path = '../data/Training/images/words/data'
train_data = pd.read_csv('csv/labels/Training.csv', encoding='UTF-8')
separate_train_images(path, train_data)


# a = '15230019010.jpg'
# print(len(a))
 