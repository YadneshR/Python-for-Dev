import os

folders = input("Please provide list of folders names with spaces in between: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)

    except FileNotFoundError:
        print("Print provide a valid folder name, looks like this folder does not exist: ")
        break
      
    print("======= listing files for the folder - "+ folder)

    for file in files:
        print(file)
