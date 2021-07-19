from Server.server import create_server;
from CommandLine.interface import command_line;
from Directory.FilesandFolder import find_subfolder,check_extension;

def main():
    print("Enter the mode you wan't to continue with => ")
    print("1 : Single File")
    print("2 : Directory")
    mode=int(input())
    if mode==1:
        print()
        print("1 : Command Line")
        print("2 : Web Based")

        choice = int(input())
        if choice == 1:
            command_line()

        if choice==2:
            create_server()
    
    else:
        print()
        print("Enter the directory")
        directory=input()
        
        find_subfolder(directory)
        check_extension()


        
        
main()