import requests
from bs4 import BeautifulSoup
import os 
import pathlib
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
imagedown("https://www.britannica.com/animal/chicken", 'output')