def get_data() -> list:
    import random  # ← Импорт внутри функции
    return random.choice([1, 2, 3])

result = get_data()
print(result)  # ✅ Работает


# А вот так НЕ работает:
# print(random.choice([1, 2, 3]))  # ❌ NameError: random не определён



################ the diff between isInstance vs type

result = "hello"
print(type(result))  # <class 'str'>

result = 42
print(type(result))  # <class 'int'>

result = [1, 2, 3]
print(type(result))  # <class 'list'>

# type() возвращает ТОЧНЫЙ класс объекта


result = "hello"
isinstance(result, str)   # True
isinstance(result, int)   # False

result = 42
isinstance(result, int)   # True
isinstance(result, str)   # False

################ ################ ################ ################ ################

class Animal:
    pass

class Dog(Animal):  # Dog наследуется от Animal
    pass

dog = Dog()

# type() - точный тип:
print(type(dog))  # <class 'Dog'>
print(type(dog) == Dog)  # True
print(type(dog) == Animal)  # False ❌ Не совпадает!

# isinstance() - проверяет класс И родителей:
print(isinstance(dog, Dog))  # True ✅
print(isinstance(dog, Animal))  # True ✅ Проверяет родителей!


################ ################ ################ ################ ################ ################



class Vehicle:
    pass

class Car(Vehicle):
    pass

car = Car()

# type() - не ловит наследование:
if type(car) == Vehicle:
    print("Vehicle")  # ❌ НЕ выведет

# isinstance() - ловит наследование:
if isinstance(car, Vehicle):
    print("Vehicle")  # ✅ Выведет!


    ################ ################ ################ ################ ################ ################ ################



    class Animal:
        def speak(self):
            return "Some sound"


    class Dog(Animal):
        def speak(self):
            return "Woof!"


    class Cat(Animal):
        def speak(self):
            return "Meow!"


    # Функция ожидает Animal:
    def make_sound(animal: Animal) -> None:
        print(animal.speak())


    dog = Dog()
    cat = Cat()

    # С type() - ЖЕСТКАЯ проверка:
    if type(dog) == Animal:
        print("It's an animal")  # ❌ НЕ выведет (dog это Dog, не Animal!)

    # С isinstance() - ГИБКАЯ проверка:
    if isinstance(dog, Animal):
        print("It's an animal")  # ✅ Выведет (Dog это подтип Animal)