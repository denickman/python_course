contents = [
    'all right reserverd',
    'fuck them all to death',
    'awesome carrot i ever see here'
]
filenames = ['doc.txt', 'report.txt', 'presentation.txt']



for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)



a = 'this is a string alone' \
    'on my onw' \
    'to be totally honest'

b = (
    'fata morgana '
    'memento more '
    'capre dias '
     )

c = '''hasta la vista
simiran yartazi
'''

print(a)

print(b)

print(c)