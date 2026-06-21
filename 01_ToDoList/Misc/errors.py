######################################################################################################

# # АРИФМЕТИЧЕСКИЕ ОШИБКИ
# ZeroDivisionError      # Деление на ноль
# OverflowError          # Число слишком большое
#
# # ТИПЫ ДАННЫХ
# TypeError              # Неправильный тип данных
# ValueError             # Правильный тип, но неправильное значение
#
# # ИНДЕКСЫ И КЛЮЧИ
# IndexError             # Индекс вне диапазона списка
# KeyError               # Ключ не найден в словаре
#
# # ФАЙЛЫ
# FileNotFoundError      # Файл не существует
# PermissionError        # Нет прав доступа
#
# # ИМЕНА ПЕРЕМЕННЫХ
# NameError              # Переменная не определена
#
# # СИНТАКСИС
# SyntaxError            # Ошибка в синтаксисе кода
# IndentationError       # Неправильный отступ
#
# # ДРУГОЕ
# AttributeError         # Атрибут не существует
# ImportError            # Ошибка импорта модуля
# RuntimeError           # Общая ошибка выполнения


#####################################################################################

# ❌ ZeroDivisionError
result = 10 / 0  # Деление на ноль

# ❌ TypeError
number = int("123") + "abc"  # Нельзя складывать int и str

# ❌ ValueError
age = int("двадцать")  # "двадцать" - не число

# ❌ IndexError
my_list = [1, 2, 3]
item = my_list[10]  # Индекса 10 нет!

# ❌ KeyError
my_dict = {'name': 'John'}
value = my_dict['age']  # Ключа 'age' нет!

# ❌ FileNotFoundError
file = open('не_существует.txt')

# ❌ NameError
#print(undefined_variable)  # Переменная не определена

# ❌ AttributeError
my_string = "hello"
my_string.hello()  # У строк нет метода hello()





#####################################################################################
try:
    # Опасный код
    pass

except ValueError:
    # Ловим ТОЛЬКО ValueError
    print("Ошибка значения")

except IndexError:
    # Ловим ТОЛЬКО IndexError
    print("Ошибка индекса")

except (TypeError, AttributeError):
    # Ловим НЕСКОЛЬКО типов сразу
    print("Ошибка типа или атрибута")

except Exception as e:
    # Ловим ВСЕ остальные ошибки
    print(f"Неизвестная ошибка: {e}")




#####################################################################################




    try:
        int("abc")
    except Exception as e:
        print(f"Тип ошибки: {type(e).__name__}")
        print(f"Сообщение: {e}")

    # Вывод:
    # Тип ошибки: ValueError
    # Сообщение: invalid literal for int() with base 10: 'abc'