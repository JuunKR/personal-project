import os 

import shutil


import cv2
from matplotlib import pyplot as plt

base_dir = '/Users/admin/Downloads'

img_dir = './test'



print(len(os.listdir(img_dir)))

print(os.listdir(img_dir))



img = cv2.imread('./test/00130001001.jpg', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()