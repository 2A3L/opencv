import cv2
img = cv2.imread("lena.jpg")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for(x,y,w,h)in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),1)
cv2.imshow('img', img)
cv2.waitKey(0)