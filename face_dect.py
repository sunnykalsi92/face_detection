#install open cv, 
#pip install python-opencv *maybe add -headless
#amazon price dector


import cv2

#load pretrained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
'''
#
img = cv2.imread('IMG_20190106_0005.jpg')
#
#convert to grayscale (have to do it)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscale)

#draw rectangles around the faces
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)


#
cv2.imshow('test1', img)
#

cv2.waitKey()
'''


#to capture video from webcam.
webcam = cv2.VideoCapture(0)

while True:
    #read the current frame
    successful_frame_read, frame = webcam.read()
    #convert to grayscale (have to do it)
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscale)
    #draw rectangles around the faces
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow('test1', frame)
    #waitkey, waits 1 milsec to move to next frame
    key = cv2.waitKey(1)
    # stop if Q key is pressed
    if key==81 or key==113:
        break
#let go of the webcam
webcam.release()

print('done')