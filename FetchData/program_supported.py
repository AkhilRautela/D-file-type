from bs4 import BeautifulSoup
import requests

def program_supported(extension):
    url = 'https://fileinfo.com/extension/'
    html_text = requests.get(url+extension).text
    soup = BeautifulSoup(html_text, 'lxml')
    platform = soup.find('div', class_='programsBox infoBox')
    try:
        opsystems = platform.find_all('div', class_='platformwrapper')
    except:
        return {} 
    supportedPrograms = {}
    for opsystem in opsystems:
        os = opsystem.find('div', class_='platform').text
        programs1 = opsystem.find('div', class_='apps')
        temp = []
        for program1 in programs1:
            name = program1.find('a')
            if name != -1:
                temp.append(name.text)
        supportedPrograms[os] = temp
    return supportedPrograms