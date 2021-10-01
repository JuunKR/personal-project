import glob
import random
import os
import pandas as pd
import shutil as sh
import os

path = '../data/Training/images/words/data'

datas = glob.glob(path + '/*')

# print(datas)

def split_train_test(datas, path):
    words = pd.read_csv('csv/ksx100.csv', encoding='UTF-8')
    ksx1001 = words['0'].values.tolist()

    for ksx in ksx1001:
        os.makedirs('../data/Training/images/words//train/' + ksx)
        os.makedirs('../data/Training/images/words//test/' + ksx)


    for data in datas:
        path = glob.glob(data + '/*')
        count = round(len(path) * 0.2)
        temp = []
        for i in random.sample(path, count):
            sh.move(i, '../data/Training/images/words/test/' + str(i[-17]))

    os.rename(path, path +'/' +'train')