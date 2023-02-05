import os
def getSomeImages(theinput):
    os.chdir("Google-Image-Scraper")
    os.system("python main.py " + theinput)
# the place where these are stored is in the Google-Image-Scraper\output\ + the name
with open('backend/static/name.txt') as f:
        name = f.readline()
getSomeImages(name)
