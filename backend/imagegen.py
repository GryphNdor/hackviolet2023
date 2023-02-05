import os
def getSomeImages(theinput):
    os.chdir("Google-Image-Scraper")
    os.system("python main.py " + theinput)
# the place where these are stored is in the Google-Image-Scraper\output\ + the name
getSomeImages("Brian+Lee")
