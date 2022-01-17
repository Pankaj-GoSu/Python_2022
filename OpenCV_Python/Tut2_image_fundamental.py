"""
Author : Pankaj Goswami
Purpose : Image Fundamental and Manipulation
Date : 17/01/2022
"""

import cv2
import random

img = cv2.imread("demo1.jpg",-1)
print(img[257][95])
print(img.shape)
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0,255) ,random.randint(0,255),random.randint(0,255)]
    
tag = img[500:700,300:500] # img[row , column]
img[100:300,200:400] = tag # So here we cut one part of image and paste it somewhere else.
img = cv2.resize(img,(500,500))
cv2.imshow("Image" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()