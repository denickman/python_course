import os


date = input("enter today day: ")
mood = input("enter your mood from 1 to 10: ")
thoughts = input("let your thoughts flow: \n")

with open(f"../journal/{date}.txt", 'w') as file:
    file.write(f'MOOD: {mood}\n')
    file.write(f'THOUGHTS: {thoughts}')

# ПОСЛЕ этого получаем список файлов
files = os.listdir('../journal/')


for filename in files:
    filepath = f'../journal/{filename}'

    with open(filepath) as file:
        content = file.read()
        print(f"--- {filename} ---")
        print(content)
        print()










