from urllib.request import urlopen
from bs4 import BeautifulSoup
import shutil
import os

class WebScraper(object):
    def __init__(self,website):
        self.website = website
        
    def __str__(self):
        print("Connecting to {}".format(self.website))

    def file_creator(self,filename):
        self.filename = filename
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
