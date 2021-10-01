from preprocessing import Preprocessing
from gather_json import Gather_json
from gather_images import Gather_images
from build_model import Build_Model
import pandas as pd
import numpy as np
import glob
    
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import datetime
import time


if __name__ == '__main__':

    pre = Preprocessing()

    #. ksx1001_csv 파일 만들기
    # pre.make_ksx1001() 
    
    #. ksx1001외의 글자가 있는지 확인       
    # pre.check_ksx1001()      

    #. jason파일에서 필요한 정보 추출 및 csv파일 만들기
    # get_json_file_train_path = '../data/Training/labels/words'
    # get_json_file_validation_path = '../data/Validation/labels/words'

    # Gather_json(get_json_file_train_path)   
    # Gather_json(get_json_file_validation_path)  

    #. 이미지 파일한 곳에 모으기
    # from_train_path = '../data/Training/images/words'
    # to_train_path = '../data/Training/images/words/data'
    # from_test_path = '../data/Validation/images/words'
    # to_test_path = '../data/Validation/images/words/data'

    # Gather_images(from_train_path , to_train_path)
    # Gather_images(from_test_path , to_test_path)

    #. 한글 분류
    # sep_img_path = '../data/Training/images/words/data'
    # sep_img_train_data = pd.read_csv('csv/labels/Training.csv', encoding='UTF-8')

    # pre.separate_train_images(sep_img_path, sep_img_train_data) 

    #. train test 분류
    # img_path = '../data/Training/images/words/data'
    # datas = glob.glob(img_path + '/*')  

    # pre.separate_train_test(datas, img_path)

    #. data

    kernel = 32

    train_generator = pre.generate_train_data(kernel)
    test_generator =  pre.generate_test_data(kernel)
    validation_generator = pre.generate_val_data(kernel)

    x_train =  np.load('../data_csv/x_train_data.npy')
    y_train =  np.load('../data_csv/y_train_data.npy')
    
    x_test =  np.load('../data_csv/x_test_data.npy')
    y_test =  np.load('../data_csv/y_test_data.npy')

    x_val =  np.load('../data_csv/x_val_data.npy')
    y_val =  np.load('../data_csv/y_val_data.npy')

    # print(x_train.shape, y_train.shape)
    # print(x_test.shape, y_test.shape)
    # print(x_val.shape, y_val.shape)

    # exit()
    pre.train_augmentation(x_train, y_train, kernel)

    x_train = np.load('../data_csv/x_a_train_data.npy')
    y_train = np.load('../data_csv/y_a_train_data.npy')

    print(x_train.shape, y_train.shape)
    print(x_test.shape, y_test.shape)
    print(x_val.shape, y_val.shape)


    '''
    (321549, 28, 28, 3) (321549, 2350)
    (55337, 28, 28, 3) (55337, 2350)
    (33114, 28, 28, 3) (33114, 2350)
    '''

    # x_train = pre.train_augmentation()[0][0]
    # # y_train = pre.train_augmentation()[0][1]
    # # print(x_train.shape, y_train.shape)

    # # x_test = pre.generate_test_data()[0][0]
    # # y_test = pre.generate_test_data()[0][1]
    # # print(x_test.shape, y_test.shape)

    # # val_x = pre.generate_val_data()[0][0]
    # # val_y = pre.generate_val_data()[0][1]

    print('모델왔어요')
    #. model
    m = Build_Model()
    model = m.build_model()
    
    #. 평가, 예측
    date = datetime.datetime.now()
    date_time = date.strftime("%m%d_%H%M")

    filepath = 'save/'
    filename = '.{epoch:04d} - {val_loss:.4f}.hdf5'
    modelpath = "".join([filepath, "songulsi", date_time, "-", filename])

    es = EarlyStopping(monitor='val_loss',patience=20, mode='auto', verbose=1, restore_best_weights=True,)

    mcp = ModelCheckpoint(moniotr='val_loss', mode = 'auto', verobs=1, save_best_only=True, filepath= modelpath)

    start_time = time.time()
    hist = model.fit(x_train, y_train, epochs=1000, validation_data=(x_val, y_val), batch_size=128, callbacks=[es, mcp])  
    model.save('save/model_save.h5')
    end_time = time.time() - start_time


    #. 평가, 예측 가즈아!

    loss = model.evaluate(x_test,y_test) 

    print('걸린시간 : ', end_time)
    print('loss : ', loss[0])
    print('acc : ', loss[1])





    