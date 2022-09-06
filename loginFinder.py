import requests
import argparse
from bs4 import BeautifulSoup
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




class LoginFinder:

    def __init__(self):
        self.urls = []
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", "-f", help="File name of urls\n")
        self.filename = parser.parse_args()
        self.editUlrs()
        self.checkUrls()

    def editUlrs(self):
        with open(self.filename.file, "r") as file:
            for i in file:
                self.urls.append(i.split("\n")[0])
    
    def checkUrls(self):
        for url in self.urls:
            try:

                req = requests.get(url, timeout=5, verify=False, allow_redirects=True)
                html = BeautifulSoup(req.text, "html.parser")
                input_checker = str(html.find_all('form'))
                
                if 'type="password"' in input_checker:
                    print(url +" Input alanı var")
                else:
                    print(url + " Input alanı yok")
               
            except requests.exceptions.ConnectionError as err:
                pass
            except requests.exceptions.ReadTimeout as err:
                    pass
            except requests.exceptions.TooManyRedirects as err:
                    pass
            except requests.exceptions.InvalidURL as err:
                    pass

if __name__ == "__main__":
    app = LoginFinder()
    