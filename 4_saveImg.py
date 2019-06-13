# pip install opencv-contrib-python
import cv2

img1 = cv2.imread('1.png', 0)   # B/W

cv2.imshow('Picture', img1)

cv2.imwrite('4_output.png', img1)

cv2.waitKey(0)    # delay till you type somekey
cv2.destroyAllWindows()