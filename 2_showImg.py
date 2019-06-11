# pip install opencv-contrib-python
import cv2

img1 = cv2.imread('1.png', 0)   # B/W
img2 = cv2.imread('1.png', 1)   # Color

print(img1) 
# output = numspy array

cv2.imshow('Hello There!', img1)
# cv2.waitKey(0)    # delay till you type somekey
cv2.waitKey(2000)   # delay 2 s
cv2.destroyAllWindows()