import os

root = "Data"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        print(directories)
        print(files)
        input()
