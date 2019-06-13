# Face Detection using Cascade Classifier

import cv2

# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread('5_messi.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

wajah = face_cascade.detectMultiScale(
    gray_img,
    scaleFactor = 1.5,
    minNeighbors = 5
)

print(wajah)
print(type(wajah))

# ===========================================
# menambahkan kotak deteksi di area wajah
# ===========================================

for x, y, w, h in wajah:
    img = cv2.rectangle(
        img,            # image object
        (x,y),          # posisi kotak
        (x+w, y+h),     # posisi kotak
        (0, 255, 0),    # warna kotak RGB
        3               # lebar garis kotak
    )

resized = cv2.resize(img, (800,600))
cv2.imshow('Lionel Messi', resized)
cv2.imwrite('5_outMessi.jpg', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()