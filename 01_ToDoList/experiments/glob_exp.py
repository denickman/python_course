import glob


myfiles = glob.glob("../txtFiles/*.txt")

for filepath in myfiles:
    with open(filepath) as file:
        print(file.read())



