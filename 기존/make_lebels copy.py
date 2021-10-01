#-*- coding: utf-8 -*-
import os
import glob
import json
import csv
from tqdm import tqdm
import time

class FindID :
    def __init__(self, path):
        self.path = path       #폴더들 주소
        self.json_list = []    #폴더들에서 json파일만 뽑아서 저장
        self.file_dic = {}     #모든 폴더와 폴더경로안의 파일들을 정리해놓은 사전.
        self.output_dic = {}   #마지막 출력을 위해서 key->json파일이름, value->각각의ID를 저장시킬거임. 

        self.add_files(path)   #file_dic사전만들기 시작
        self.creat_output()    #출력할 내용을 정리하는 output_dic에 값을 넣어주는 함수.

    def my_list(self, file_path):
        file_list = glob.glob(file_path + "/*")
        return file_list
    
    def check_json(self, file_name):
        '''
            만약 json파일까지 도달했다면(파일이름이 .json으로 끝난다면), 그 json파일은 json_list에 저장하고,
            아직 폴더가 남았다면, 다시 add_files()를 호출해서 file_dic사전에 추가정리. 
        '''
        if(self.file_dic[file_name][0].endswith(".json")):
            self.json_list.extend(self.file_dic[file_name])
        else:
            for name in self.file_dic[file_name]:
                self.add_files(name)

    def add_files(self, file_path):
        '''
            main함수
            my_list로 폴더안의 파일리스트를 받아서 file_dic에 저장.
            그리고 json 파일까지 도달했는지 체크한다.
        '''
        self.file_dic[file_path] = self.my_list(file_path)
        self.check_json(file_path)

    def creat_output(self):
        '''
            이제 다 뽑아낸 json_list(시리얼넘버)들로 각각의 json파일안의 'sampleId'의 value값을 뽑아,
            output_dic사전에 저장한다. 
        '''
        for filename in self.json_list:
            with open(filename, 'r',encoding="utf8") as file:
                json_data = json.load(file)
            self.output_dic[filename] = json_data['info']['text']

if __name__ == "__main__":
    # folder_name = input("input folder address : ")
    folder_name = ['./_file/data/label_data/', './_file/validation/label_validation/'] 

    # ./_file/data/label_data/
    # ./_file/validation/label_validation/

    #파이썬 파일과 폴더가 동일할 때는 이 코드를 씀.
    #folder_name = "./" + folder_name
    for path in folder_name:
        folder_name = path
        folder = FindID(folder_name)

        '''
            output_dic(키:json파일경로, 발류: ID값)사전에 있는 값을 csv에 옯겨적는다.
            시리얼넘버는 키값인 json파일경로에서 뽑아냈다. -> key.split("/")[-1][:-8]
        '''
        with open('./_csv/labels/' + folder_name.split("/")[-2] + '.csv','w',encoding="utf8", newline='') as csvfile :
            writer = csv.writer(csvfile)
            writer.writerow(['path','File_Name', 'word'])
            for key, val in tqdm(folder.output_dic.items()):
                writer.writerow([key,key.split("/")[-1][-16:-5], val])
