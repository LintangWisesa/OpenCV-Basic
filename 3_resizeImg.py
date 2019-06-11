# pip install opencv-contrib-python
import cv2

img1 = cv2.imread('1.png', 0)   # B/W
resized1 = cv2.resize(img1, (300, 600))
resized2 = cv2.resize(img1, (int(img1.shape[1]*2), int(img1.shape[0]*2)))

cv2.imshow('It\'s 300 x 600', resized1)
cv2.imshow('2 times bigger', resized2)

cv2.waitKey(0)    # delay till you type somekey
cv2.destroyAllWindows()