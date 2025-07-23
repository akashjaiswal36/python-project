import os

folders = input("Please provide list of folders names with spaces in between: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Pleease provide valid folder name")
        continue

    print("==========>pringint files for folder: " + folder)
    
    for file in files:
        print(file)