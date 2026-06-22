


text = "a b c d e"

result = text.split(' ', 1)  # 1 разделение = 2 части
print(result)
# ['a', 'b c d e']

result = text.split(' ', 2)  # 2 разделения = 3 части
print(result)
# ['a', 'b', 'c d e']

result = text.split(' ', 3)  # 3 разделения = 4 части
print(result)
# ['a', 'b', 'c', 'd e']




text = "Hello World"
text[:5]      # "Hello"
text[6:]      # "World"
text[::2]     # "HloWrd" (каждый 2-й символ)
text[::-1]    # "dlroW olleH" (в обратном порядке)


numbers = [1, 2, 3, 4, 5]
numbers[:3]   # [1, 2, 3]
numbers[1:]   # [2, 3, 4, 5]
numbers[::2]  # [1, 3, 5]



data = (10, 20, 30, 40, 50)
data[:2]      # (10, 20)
data[1:4]     # (20, 30, 40)
data[::-1]    # (50, 40, 30, 20, 10)


r = range(1, 11)  # 1, 2, 3... 10
r[:5]             # range(1, 6) → [1, 2, 3, 4, 5]


email = "user@example.com"
username = email[:email.index('@')]  # "user"

file_path = "/home/user/file.txt"
filename = file_path.split('/')[-1]  # "file.txt"

todos = ['Задача 1\n', 'Задача 2\n', 'Задача 3\n']
first_half = todos[:len(todos)//2]  # Первую половину

coordinates = (10, 20, 30, 40, 50)
x, y, z = coordinates[:3]  # x=10, y=20, z=30

# dict и set НЕ упорядочены (в старых версиях Python)
# Поэтому "первые 2 элемента" не имеют смысла

my_dict = {'name': 'John', 'age': 30, 'city': 'NY'}
# Какие 2 элемента взять? Непонятно!

# Если нужно — преобразуй в список:
list(my_dict.keys())[:2]    # ['name', 'age']
list(my_dict.values())[:2]  # ['John', 30]


