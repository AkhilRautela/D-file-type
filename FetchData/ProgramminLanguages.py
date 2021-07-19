from bs4 import BeautifulSoup
import requests

from collections import defaultdict

programming_language = []


def get_programming_language():

    global programming_language

    data = requests.get(
        "https://en.wikipedia.org/wiki/List_of_programming_languages")

    soup = BeautifulSoup(data.content, 'html.parser')

    container_lang = soup.findAll('div', class_="div-col")

    for list_item in container_lang:
        one_list = list_item.text.split("\n")
        for language in one_list:
            if language != "":
                programming_language.append(language.split(" ")[0])
