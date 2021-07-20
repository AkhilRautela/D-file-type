import requests
import wikipedia

from bs4 import BeautifulSoup

from FetchData.ProgramminLanguages import *
from threading import *

import requests

url = "https://fileinfo.com/extension/"
url1 = "https://filext.com/file-extension/"
def fetchfromfirst(url,extension):
    response = requests.get(url + extension)
    soup = BeautifulSoup(response.content, 'html.parser')

    left = soup.find('div', class_="infoBox")

    summary1 = left.text.strip()
    return summary1
def fetchfromsecond(url1,extension):
    response = requests.get(url1 + extension)
    soup = BeautifulSoup(response.content, 'html.parser')

    info1 = soup.find('p').text.strip()
    return info1
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)

        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return

def fetch_extension_data(extension):

    try:
        print("Extension", extension)
        print("Loading ...")

        # print(wikipedia.summary(".py"))

        t1 = ThreadWithReturnValue(target=fetchfromfirst, args=(url,extension,))
        t2 = ThreadWithReturnValue(target=fetchfromsecond, args=(url1,extension,))
        
        
        t3=Thread(target=get_programming_language)
        t1.start()
        t3.start()
        t2.start()
        summary=t1.join()
        t3.join()
        info=t2.join()
        

 
        

        is_programming_language = False
        prog_language = ""

        info = info.replace(".", "")
        info = info.replace(",", "")


        for language in programming_language:
            if language.lower() in map(lambda x:x.lower(),info.split(" ")):
                is_programming_language = True
                prog_language = language
                break

        if is_programming_language:
            return [summary,prog_language]

        return [summary]
    except:
        return []

