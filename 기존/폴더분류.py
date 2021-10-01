import shutil
import numpy as np
import pandas as pd
from tqdm import tqdm

label_data = pd.read_csv('./_csv/labels/label_data.csv',  encoding='UTF-8')
label_validation = pd.read_csv('./_csv/labels/label_validation.csv',  encoding='UTF-8')
words = pd.read_csv('./_csv/ksx100.csv', encoding='UTF-8')
words = np.array(words)

label_data = np.array(label_data)
label_validation = np.array(label_validation)


label_data = label_data[:,1]
words = words.reshape(2350,)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# 딕셔너리 만들기
kxs100 = {}
for i,j in enumerate(words):
    kxs100[str(j)] = i


'https://chancoding.tistory.com/93'
# trainFileList = [x for x in label_data if 'jpg' in x]
currentPath = 11111111111


import shutil 
from_ = './mydir/myfile.txt' 
to_ = './yourdir' 
shutil.move(from_, to_)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 폴더 만들어주기 train
currentPath = path + 'train'  # train 파일이 있는 현재 경로

print(word.keys()) # ga, da, sa ..

# 카테고리화 된 폴더가 없으면 폴더 생성
try:
    for key in word.keys(): 
        os.makedirs(currentPath + f'\\{key}')
# 이미 존재하면 패스
except:
    pass

# jpg 파일 옮기기
for file in trainFileList: # Train data들 각각
    label = file.split('_')[0] 
    # 예시 aa_bc_01_02.jpg
    # label = 'aa'
    targetPath = currentPath + f'\\{label}' # 목표 위치인 aa폴더에 넣기
    try :
        shutil.move(currentPath+f'\\{file}', targetPath+f'\\{file}')
    except:
        pass