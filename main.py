from urllib.request import urlopen
from bs4 import BeautifulSoup
import shutil
import time
import os

class WebScraper(object):
    def __init__(self):
        self.website = input("Enter a website: ")
        time.sleep(2)
        self.__str__()
        time.sleep(2)
        self.file_creator()
        time.sleep(2)
        print("{} file was created successfully".format(self.filename))
        time.sleep(2)
        self.file_handler(self.filename)
        self.file_mover()
        
    def __str__(self):
        print("Connecting to {}".format(self.website))


    def file_creator(self):
        self.filename = input("Enter a filename: ")
        if os.access(self.filename, os.R_OK):
            with open(self.filename,"w+") as f:
                return f

    def file_handler(self,filename):
        html_data = urlopen(self.website)
        soup = BeautifulSoup(html_data.read(), "html.parser")
        f = open(self.filename, "w+")
        for link in soup.find_all("a"):
            print(link.get("href"))
            f.write(link.get("href")+ "\n")

    def file_mover(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        current_path = os.getcwd() + "\\" + self.filename
        shutil.move(current_path, desktop)



