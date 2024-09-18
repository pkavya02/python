import os

folders = input("Enter the folder names with spaces between them: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide the correct folder name")  
        break
    except PermissionError:
        print("Person don't have permission")
        break      

    print("******listing files in the folder:" + folder)
    for file in files:
        print(file)
