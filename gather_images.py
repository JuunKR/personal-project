import glob
import shutil as sh
from tqdm import tqdm

class Gather_images(object):
    def __init__(self ,from_path, to_path):
        self.from_path = from_path
        self.to_path = to_path

        self.file_list = []
        self.find_file_path()
        self.file_move()
    #     self.gather_images()
        
    # def gather_images(self):
    #     for path in self.from_path:
    #         self.find_file_path(path)
    #         self.file_move(path)

    def find_file_path(self):
            ### 대상 파일 경로 확인 ###
        file_list = glob.glob(self.from_path + '/**/*' )
        self.file_list =  file_list
        # print(self.file_list)
    
    def file_move(self):
        ### 대상 파일 이동 ###
        for file in tqdm(self.file_list):
            file_name = file.split('\\')[-1] # file_name = 파일명.type
            sh.move(file ,self.to_path + '/' + file_name)

 

# if __name__ == '__main__':

#     # from_path = '../data/Training/images/words'
#     # to_path = '../data/Training/images/words/data'

#     from_path = '../data/Validation/images/words'
#     to_path = '../data/Validation/images/words/data'
    
#     g = Gather_images(from_path , to_path)
    
