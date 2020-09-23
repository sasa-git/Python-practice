import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,640)

# read Classfier models
face_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    metadata = f'Width: {cap.get(3)}, Height: {cap.get(4)}, FPS: {cap.get(5)}'
    cv2.putText(img,metadata,(10,450), font, 0.8,(0,0,255),1,cv2.LINE_AA)
    detection = f'{len(faces)} detected!'
    cv2.putText(img,detection,(10,20), font, 0.8,(0,0,255),1,cv2.LINE_AA)

    cv2.imshow('img', img)

    # Display the resulting frame
    # cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()