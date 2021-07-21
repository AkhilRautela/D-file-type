from FetchData.Fetch import *
from FetchData.program_supported import program_supported
import json
def command_line():
    print()
    print("Enter The File directory")
    dir = input()
    print()
    if "\\" in dir:
        file_name = dir.split("\\")[-1]
    else:
        file_name = dir.split("/")[-1]

    file_extension = file_name.split(".")[-1]

    response = fetch_extension_data(file_extension)
    programs = program_supported(file_extension)

    print()

    if len(response)==0:
        print("No Extension Found")
    
    elif len(response)==1:
        print("##### SUMMARY #####\n")
        print(response[0])
        print()
        if programs != None:
            print("##### Progams Supported #####")
            print(json.dumps(programs,sort_keys=False,indent=4))
        
    else:
        print("PROGRAMMING LANGUAGE  => ",response[1])
        print()
        print("##### SUMMARY #####\n")
        print(response[0])
        print()
        if programs != None:
            print("\n##### Progams Supported #####")
            print(json.dumps(programs,sort_keys=False,indent=4))
    


