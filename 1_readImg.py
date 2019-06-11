# pip install opencv-contrib-python
import cv2

img1 = cv2.imread('1.png', 0)   # B/W
img2 = cv2.imread('1.png', 1)   # Color

print(img1) 
# output = numspy array