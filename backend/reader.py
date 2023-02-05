import os
import shutil
def movethatfile():
    os.chdir("Google-Image-Scraper")
    #copy the file writeme.txt to the file of the same name in backend
    shutil.copy("writeme.txt", "backend/output/allURLS.txt")