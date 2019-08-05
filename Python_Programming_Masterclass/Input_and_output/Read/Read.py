
with open("sample.txt", "r") as file:
    data = file.readlines()
    for line in data:
        print(line, end="")