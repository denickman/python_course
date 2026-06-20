waiting_list = ['den', 'roma', 'john', 'alex']
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f'{index+1}.{item.capitalize()}'
    print(row)


print("==================")


# First Option

filenames = ["1.doc", "1.report", "1.presentation"]

# '1-doc.txt', '1-report.txt', '1-presentation.txt'

newFilenames = []

for item in filenames:
    newItem = f"{item.replace(".", "-")}.txt"
    newFilenames.append(newItem)

print("Result 1")
print(newFilenames)

# Second Option

filenames = [filename.replace(".", "-") + '.txt' for filename in newFilenames]
print("Result 2")
print(filenames)





new = []

for i in [1, 2, 3]:
    new.append(i + 10)

print(new)


new = [i for i in ['a', 'b', 'c']]
print(new)