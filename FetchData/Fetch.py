import requests
import wikipedia

from bs4 import BeautifulSoup

from FetchData.ProgramminLanguages import *

import requests

url = "https://fileinfo.com/extension/"
url1 = "https://filext.com/file-extension/"


def fetch_extension_data(extension):

    try:
        print("Extension", extension)
        print("Loading ...")

        # print(wikipedia.summary(".py"))

        response = requests.get(url + extension)
        soup = BeautifulSoup(response.content, 'html.parser')

        left = soup.find('div', class_="infoBox")

        summary = left.text.strip()

        get_programming_language()

        response = requests.get(url1 + extension)
        soup = BeautifulSoup(response.content, 'html.parser')

        info = soup.find('p').text.strip()

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
