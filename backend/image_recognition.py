import cv2
import numpy as np
import face_recognition

debug = False

# load real image
img_bgr = face_recognition.load_image_file('real_linus.jpg')
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
cv2.waitKey

# color map
img_modi=face_recognition.load_image_file('real_linus.jpg')
img_modi_rgb = cv2.cvtColor(img_modi,cv2.COLOR_BGR2RGB)
#--------- Detecting Face -------
face = face_recognition.face_locations(img_modi_rgb)[0]
copy = img_modi_rgb.copy()
# ------ Drawing bounding boxes around Faces------------------------
cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)
if(debug):
    cv2.imshow('Original_Detected', copy)
cv2.waitKey

img_modi = face_recognition.load_image_file('real_linus.jpg')
img_modi = cv2.cvtColor(img_modi,cv2.COLOR_BGR2RGB)

#------to find the face location
face = face_recognition.face_locations(img_modi)[0]

#--Converting image into encodings
train_encode = face_recognition.face_encodings(img_modi)[0]

#----- lets test an image
test = face_recognition.load_image_file('fake_linus.jpg')
test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
test_encode = face_recognition.face_encodings(test)[0]
found = face_recognition.compare_faces([train_encode],test_encode)
if(found):
    print("the image has been found")
else:
    print("the image has not been found")
cv2.rectangle(img_modi, (face[3], face[0]),(face[1], face[2]), (255,0,255), 1)
if(debug):
    cv2.imshow('Fake', test)
cv2.waitKey(0)