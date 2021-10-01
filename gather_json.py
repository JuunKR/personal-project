#-*- coding: utf-8 -*-
import os
import glob
import json
import csv
from tqdm import tqdm
import time

'''
AIhub에서 제공된 데이터가 여러 폴더에 json파일(라벨데이터) 나뉘어 있음
한곳에 모으기 위한 코드
'''

class Gather_json(object) :
    def __init__(self, path):
        self.path = path        # 폴더들 주소
        self.json_list = []     # 폴더중에서 json만 선별
        self.file_dic = {}      # 
        self.output_dic = {}

        self.gather(path)


    def gather(self, file_path):
        self.add_files(file_path)
        self.make_label()
        with open('csv/labels/' + file_path.split("/")[-3] + '.csv','w',encoding="utf8", newline='') as csvfile :
            writer = csv.writer(csvfile)
            writer.writerow(['path','File_Name', 'img_name', 'word'])
            for key, val in tqdm(self.output_dic.items()):
                writer.writerow([key,key.split("/")[-1][-16:-5], str(key.split("/")[-1][-16:-5]) + '.jpg', val])



    def make_list(self, file_path):
        '''
        path 안의 폴더들을 리스트로 정리해서 return
        glob 파일들의 리스트를 뽑을 때 사용
        '''
        file_list = glob.glob(file_path + '/*')
        # print(len(file_list))
        return file_list

    def add_files(self, path):
        '''
        {path : [files names]}
        '''
        self.file_dic[path] = self.make_list(path)
        if(self.file_dic[path][0].endswith(".zip")):
            del_path = self.file_dic[path][0]
            os.remove(del_path)
            self.file_dic[path] = self.make_list(path)
        self.check_json(path)


    def check_json(self, path_name):
        '''
        .endsWith() 특정열로 끝나는지 확인하는 메서드
        .extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣음.
        json 으로 파일이름이 끝나면 list에 저장하고,
        폴더가 남아있다면, 다시 add_files()를 호출하고 dic 정리
        '''
        # print(self.file_dic)
        if(self.file_dic[path_name][0].endswith(".json")):
            self.json_list.extend(self.file_dic[path_name])
        else:
            for name in self.file_dic[path_name]:
                self.add_files(name)

    def make_label(self):
        '''
            이제 다 뽑아낸 json_list(시리얼넘버)들로 각각의 json파일안의 
            필요한 라벨을 저장
        '''
        for file_name in tqdm(self.json_list):
            with open(file_name, 'r',encoding="utf8") as file:
                json_data = json.load(file)
            self.output_dic[file_name] = json_data['info']['text']        

# if __name__ == '__main__':
#     file_train_path = '../data/Training/labels/words'
#     file_validation_path = '../data/Validation/labels/words'

#     Gather_json(file_validation_path)


