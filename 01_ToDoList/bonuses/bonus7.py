

# Пример который показывает проблему:
with open('file.txt', 'r') as file:
    content1 = file.read()
    print(content1)  # выводит: "Hello World"

    content2 = file.read()
    print(content2)  # выводит: "" (пусто!)



# Файл: "Hello World"
#        ↑
#     Указатель (в начале)
#
# После первого read():
# file.read() прочитал всё и передвинул указатель в конец
#
# Файл: "Hello World"
#                     ↑
#                   Указатель (в конце)
#
# Второй read():
# Указатель уже в конце, больше нечего читать → вернул ""


# Как это исправить — используй seek(0):
with open('file.txt', 'r') as file:
    content1 = file.read()
    print(content1)  # "Hello World"

    file.seek(0)  # ← переместить указатель в начало

    content2 = file.read()
    print(content2)  # "Hello World" (работает!)



# Или просто сохрани в переменную:
with open('file.txt', 'r') as file:
    content = file.read()  # читаем один раз
    print(content)  # используем столько раз сколько хочешь
    print(content)
    print(content)


# Тоже самое и для realines
with open('file.txt', 'r') as file:
    lines1 = file.readlines()
    print(lines1)  # ['Line 1\n', 'Line 2\n']

    file.seek(0)  # ← вернуться в начало

    lines2 = file.readlines()
    print(lines2)  # ['Line 1\n', 'Line 2\n'] (работает!)




 ##################################






with open('../files/doc.txt') as file:
    for line in file:  # ← это работает как readlines но эффективнее
        print(line.strip())



with open('../files/doc.txt') as file:
    content = file.read()
    print(type(content))  # <class 'str'>
    print(content)



with open('../files/doc.txt') as file:
    lines = file.readlines()
    print(type(lines))  # <class 'list'>
    print(lines)

