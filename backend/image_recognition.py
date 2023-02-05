import cv2
import numpy as np
import face_recognition
import pathlib
import requests
from bs4 import BeautifulSoup
import os 
import shutil
import glob

# debug flag
debug = True

# clear directories
shutil.rmtree('backend/output')
os.mkdir('backend/output') 

shutil.rmtree('backend/data')
os.mkdir('backend/data')

# ----- start ----

# move images from directory and renames them
def moveImages(name):
    filteredname = name.replace('+','').replace(' ','')
    for w in range(1,20):
        try:
            os.rename("Google-Image-Scraper/photos/" + name +'/'+filteredname + str(w) + '.jpeg', 'backend/output/' + str(w) + '.jpeg' )
        except:
            try:
                os.rename("Google-Image-Scraper/photos/" + name +'/'+filteredname + str(w) + '.png', 'backend/output/' + str(w) + '.png' )
            except:
                os.rename("Google-Image-Scraper/photos/" + name +'/'+filteredname + str(w) + '.jpg', 'backend/output/' + str(w) + '.jpg' )

# verify individual image
def verifyImages(index,currentCount):
    try:
        image = face_recognition.load_image_file('backend/output/'+str(index)+'.jpeg')
    except:
        try:
            image = face_recognition.load_image_file('backend/output/'+str(index)+'.png')
        except:
            image = face_recognition.load_image_file('backend/output/'+str(index)+'.jpg')
    face_locations = face_recognition.face_locations(image)
    if not face_locations:
        if(debug):print('nothing found')
    else:
        if(debug):print('face detected')
        try:
            os.rename('backend/output/'+str(index)+'.jpeg', 'backend/data/' + str(currentCount) + '.jpeg')
        except:
            try:
                os.rename('backend/output/'+str(index)+'.png', 'backend/data/' + str(currentCount) + '.png')
            except:
                os.rename('backend/output/'+str(index)+'.jpg', 'backend/data/' + str(currentCount) + '.jpg')
        currentCount +=1
    return currentCount

# load real image
img_bgr = face_recognition.load_image_file('backend/static/neps2.jpg')
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
cv2.waitKey

# color map
img_modi=face_recognition.load_image_file('backend/static/neps2.jpg')
img_modi_rgb = cv2.cvtColor(img_modi,cv2.COLOR_BGR2RGB)

# detect face
face = face_recognition.face_locations(img_modi_rgb)[0]
copy = img_modi_rgb.copy()
# draw rectangle around face
cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)
if(debug):
    cv2.imshow('Input', copy)
cv2.waitKey
# load face to compare

img_modi = face_recognition.load_image_file('backend/static/neps2.jpg')
img_modi = cv2.cvtColor(img_modi,cv2.COLOR_BGR2RGB)

# find vectors
face = face_recognition.face_locations(img_modi)[0]

# encode images
train_encode = face_recognition.face_encodings(img_modi)[0]

# check if image is the same
def findImage(index):
    try:
        test = face_recognition.load_image_file('backend/data/'+str(index)+'.jpeg')
    except:
        try:
            test = face_recognition.load_image_file('backend/data/'+str(index)+'.jpg')
        except:
            test = face_recognition.load_image_file('backend/data/'+str(index)+'.png')

    test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
    test_encode = face_recognition.face_encodings(test)[0]
    found = face_recognition.compare_faces([train_encode],test_encode)
    if(debug):print(found)
    cv2.rectangle(img_modi, (face[3], face[0]),(face[1], face[2]), (255,0,255), 1)
    if(debug):
        cv2.imshow('Fake'+str(index)+'.', test)
    cv2.waitKey

def runAnalysis():
    moveImages('Alec+Neps')
    currentCount = 0
    for x in range(1,20):
        currentCount = verifyImages(x, currentCount)
    for y in range(currentCount):
        findImage(y)
    # wait on done
    cv2.waitKey(0)
    

runAnalysis()