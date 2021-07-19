import os
from collections import defaultdict
from FetchData.Fetch import fetch_extension_data
from Server.server import create_summary_stats_server

files=[]

extension_count=defaultdict(lambda:0)

def find_subfolder(path,dist="-"):
    if os.path.isdir(path):
        print(dist+"|"+os.path.basename(path))
        for subfiles in os.listdir(path):
            find_subfolder(path+"/"+subfiles,"  "+dist)

    else:
        try:
            file_name=os.path.basename(path)
            file_extension=file_name.split(".")[-1]
            extension_count[file_extension]+=1
            print(dist+"|",file_name)
        except:
            pass


extension_summary=defaultdict(lambda:[])

def check_extension():

    print("Frequency count of extension")

    for extension,frequeny in extension_count.items():
        print(extension,frequeny)
        if extension in extension_summary:
            continue
        response = fetch_extension_data(extension)
        extension_summary[extension]=response

    for x in list(extension_summary.keys()):
        if len(extension_summary[x])==0:
            del extension_summary[x]
            del extension_count[x]

    create_summary_stats_server(extension_summary,extension_count)
    




