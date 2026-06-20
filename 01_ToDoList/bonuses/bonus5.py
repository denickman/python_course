


# Способ 1 — явно указываешь режим чтения
with open('../files/doc.txt', 'r') as file:
    print(file.read())  # ← здесь прочитал и вывел

    # or you can store into var - content = file.read()

file.read() # ← ошибка! файл уже закрыт после with


# # Способ 2 — режим 'r' подразумевается по умолчанию
# with open('files/doc.txt') as file:
#     print(file.read())
#
# # Добавление в конец (НУЖНО писать 'a'!)
# with open('file.txt', 'a') as file:
#     file.write("ещё текст")