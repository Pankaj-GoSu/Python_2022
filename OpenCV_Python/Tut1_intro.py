"""
Open CV is open source , computer vision library.
"""
import cv2

img = cv2.imread("D:\Code_For_Life\Python\Python_2022\OpenCV_Python\demo1.jpg",1)

# For Resize The Image.
img = cv2.resize(img,(400,400)) # or cv2.resize(img,(0,0),fx = 0.5,fy = 0.5) here we half the x and half the height y. of image

# For Rotate The Image.

img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

# To Save A image:
cv2.imwrite("New_img.jpg",img)
cv2.imshow("image",img)
cv2.waitKey(0) # 0 means wait for infinie amount of time.
cv2.destroyAllWindows() 