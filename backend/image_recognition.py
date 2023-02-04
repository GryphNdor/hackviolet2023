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

shutil.rmtree('backend/output')
os.mkdir('backend/output') 

#takes in a url and a folder name and downloads all the images from the url to the folder
def imagedown(url, folder):
    try:
        #if the folder doesn't exist, create it
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    #make a request to the url to get the html data
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    #identify all of the images on the page
    images = soup.find_all("img")
    count = 0
    for image in images: #for each image on the page, find it's extension and name (for the sake of naming the file)
        name = image['alt']
        link = image['src']
        bettername = pathlib.Path(name.replace(' ', '-').replace('/','') + '.jpg')
        #Write the image data to a new image file in the target folder, using the name of the file as the name of the image
        with open(name.replace(' ', '-').replace('/','') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            #print to the shell to verify that the image is being written
            print('Writing: ', name)
        renamed = pathlib.Path('backend/output/' + str(count) + '.jpg')
        bettername.rename(renamed)
        count += 1      

#example function call 
imagedown("https://www.britannica.com/technology/computer", 'output')

# load real image
img_bgr = face_recognition.load_image_file('backend/real_linus.jpg')
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
cv2.waitKey

# color map
img_modi=face_recognition.load_image_file('backend/real_linus.jpg')
img_modi_rgb = cv2.cvtColor(img_modi,cv2.COLOR_BGR2RGB)
#--------- Detecting Face -------
face = face_recognition.face_locations(img_modi_rgb)[0]
copy = img_modi_rgb.copy()
# ------ Drawing bounding boxes around Faces------------------------
cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)
if(debug):
    cv2.imshow('Original_Detected', copy)
cv2.waitKey

img_modi = face_recognition.load_image_file('backend/real_linus.jpg')
img_modi = cv2.cvtColor(img_modi,cv2.COLOR_BGR2RGB)

#------to find the face location
face = face_recognition.face_locations(img_modi)[0]

#--Converting image into encodings
train_encode = face_recognition.face_encodings(img_modi)[0]

#----- lets test an image
test = face_recognition.load_image_file('backend/fake_linus.jpg')
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