# 📚 ШПАРГАЛКА: ИМПОРТЫ И МОДУЛИ В PYTHON

---

## 🎯 ОСНОВНЫЕ ПОНЯТИЯ

### Модуль
- **Модуль = файл .py**
- Пример: `functions.py` это модуль с именем `functions`
- Содержит: функции, классы, переменные

### Пакет
- **Пакет = папка с `__init__.py`**
- Пример: папка `todos/` с файлом `todos/__init__.py`
- Содержит: модули (файлы .py) или другие пакеты

### Класс
- **Класс = шаблон для создания объектов**
- С большой буквы: `FastAPI`, `TodoApp`
- Требует создания объекта перед использованием

### Функция
- **Функция = действие/операция**
- С маленькой буквы: `get_todos`, `create_engine`
- Можешь вызвать сразу

---

## 📥 ТИПЫ ИМПОРТОВ

### 1️⃣ ИМПОРТИРОВАТЬ ВЕСЬ МОДУЛЬ

```python
import os
import json
import mymodule

# Используешь с точкой:
os.path.exists()
json.loads()
mymodule.get_todos()
```

**Когда использовать:** 
- Много функций в модуле
- Хочешь ясность откуда функция

---

### 2️⃣ ИМПОРТИРОВАТЬ КОНКРЕТНОЕ ИЗ МОДУЛЯ

```python
from os import path
from json import loads
from mymodule import get_todos, write_todos

# Используешь прямо (без модуля):
path.exists()
loads()
get_todos()
```

**Когда использовать:**
- Нужны только 1-2 функции
- Хочешь короче писать

---

### 3️⃣ ИМПОРТИРОВАТЬ С ПЕРЕИМЕНОВАНИЕМ (alias)

```python
import numpy as np
from flask import Flask as app
from .feet_to_meters import convert as feet_to_meters

# Используешь:
np.array([1, 2, 3])
app()
feet_to_meters(5, 10)
```

**Когда использовать:**
- Длинное имя модуля
- Конфликт имен (две функции одинаково названы)

---

### 4️⃣ ОТНОСИТЕЛЬНЫЙ ИМПОРТ (из текущей папки)

```python
# Из текущей папки:
from .todosFunctions import get_todos
from .filesChecker import ensure_file_exists

# Из родительской папки:
from ..utils import helper
```

**Важно:** только в пакетах (папках с `__init__.py`)

---

## 📁 СТРУКТУРА ПРОЕКТА И ИМПОРТЫ

### ПРОСТАЯ СТРУКТУРА (БЕЗ пакетов)

```
project/
├── main.py
├── functions.py
└── helpers.py
```

```python
# main.py
import functions
import helpers

# Используешь:
functions.get_todos()
helpers.format_output()
```

---

### ПРАВИЛЬНАЯ СТРУКТУРА (С пакетами)

```
project/
├── main.py
└── todos/
    ├── __init__.py           ← ВОЛШЕБНЫЙ ФАЙЛ!
    ├── todosFunctions.py
    ├── filesChecker.py
    └── validators.py
```

```python
# todos/__init__.py
from .todosFunctions import get_todos, write_todos
from .filesChecker import ensure_file_exists

# main.py
from todos import get_todos, write_todos, ensure_file_exists
```

---

### БОЛЬШОЙ ПРОЕКТ (ВЛОЖЕННЫЕ пакеты)

```
project/
├── main.py
├── converters/
│   ├── __init__.py
│   ├── feet_to_meters.py
│   └── kg_to_pounds.py
├── validators/
│   ├── __init__.py
│   └── number_validator.py
└── utils/
    ├── __init__.py
    └── helpers.py
```

```python
# main.py
from converters import feet_to_meters, kg_to_pounds
from validators import validate_number
from utils import helper
```

---

## 🔴 ЦИКЛИЧЕСКИЕ ИМПОРТЫ (ОШИБКА!)

### ❌ НЕПРАВИЛЬНО: Циклический импорт

```
main.py
  ↓ from todos import get_todos
__init__.py
  ↓ from .todosFunctions import get_todos
todosFunctions.py
  ↓ from todos import ensure_file_exists  ❌ ЦИКЛ!
```

**Ошибка:** `ImportError: cannot import name...`

### ✅ ПРАВИЛЬНО: Прямой импорт из модуля

```
main.py
  ↓ from todos import get_todos
__init__.py
  ↓ from .todosFunctions import get_todos
todosFunctions.py
  ↓ from .filesChecker import ensure_file_exists ✅ БЕЗ цикла!
```

**Правило:** Импортируй из того файла, где это ОПРЕДЕЛЕНО!

```python
# ❌ НЕПРАВИЛЬНО
from todos import ensure_file_exists

# ✅ ПРАВИЛЬНО
from .filesChecker import ensure_file_exists
```

---

## 🪄 `__init__.py` - ВОЛШЕБНЫЙ ФАЙЛ

### ЧТО ЭТО?
- Файл в папке, который делает папку ПАКЕТОМ
- Python читает его автоматически при импорте папки
- Может быть пустым!

### ДЛЯ ЧЕГО?
- Собирает импорты из разных файлов в одно место
- Определяет что доступно при импорте пакета
- Упрощает использование пакета

### ПРИМЕР

```python
# todos/__init__.py
from .todosFunctions import get_todos, write_todos
from .filesChecker import ensure_file_exists

# Теперь можно в main.py:
from todos import get_todos, write_todos, ensure_file_exists
# Вместо:
from todos.todosFunctions import get_todos
from todos.filesChecker import ensure_file_exists
```

---

## 🪟 `__name__` - СПЕЦИАЛЬНАЯ ПЕРЕМЕННАЯ

### ЧТО ЭТО?
```python
__name__  # Переменная, которая показывает как запущен файл
```

### ЗНАЧЕНИЯ

| Сценарий | `__name__` | Условие выполнится? |
|----------|-----------|------------------|
| `python file.py` | `"__main__"` | ✅ ДА |
| `import file` | `"file"` | ❌ НЕТ |

### ИСПОЛЬЗОВАНИЕ

```python
if __name__ == "__main__":
    # Этот код выполнится ТОЛЬКО при прямом запуске
    # НЕ выполнится при импорте
    print("Файл запущен напрямую")
```

### ПРИМЕРЫ

**Пример 1: Запуск напрямую**

```bash
python mymodule.py
```

```python
# mymodule.py
print("Код выполнен")

if __name__ == "__main__":
    print("Файл запущен напрямую")  ✅ Выведет
```

**Пример 2: Импорт в другой файл**

```python
# main.py
import mymodule
```

```bash
python main.py
```

```python
# mymodule.py
print("Код выполнен")  ✅ Выведет (всегда)

if __name__ == "__main__":
    print("Файл запущен напрямую")  ❌ НЕ выведет
```

---

## 🎯 КЛАССЫ vs ФУНКЦИИ

### ФУНКЦИЯ - используешь сразу

```python
# functions.py
def get_todos():
    return ["хлеб", "ДЗ"]

# main.py
from functions import get_todos

todos = get_todos()  # ✅ Прямой вызов
```

### КЛАСС - создаешь объект потом используешь

```python
# classes.py
class TodoApp:
    def __init__(self):
        self.todos = []
    
    def add(self, text):
        self.todos.append(text)

# main.py
from classes import TodoApp

app = TodoApp()      # ✅ Создание объекта
app.add("хлеб")      # ✅ Использование метода
```

---

## 📊 ШПАРГАЛКА ПО СИНТАКСИСУ

### Импорт модуля

```python
import os                          # ← Весь модуль
import numpy as np                 # ← С alias
from os import path                # ← Конкретное
from os import path as p           # ← Конкретное с alias
from . import module               # ← Относительный импорт
from .module import function       # ← Относительный конкретный
```

### В `__init__.py`

```python
# Собираем импорты из разных файлов
from .functions import get_todos, write_todos
from .validators import validate_email
from .constants import MAX_SIZE
```

### Проверка при запуске

```python
if __name__ == "__main__":
    print("Код для тестирования")
```

---

## ✅ ПРАВИЛА И РЕКОМЕНДАЦИИ

### ✅ ДЕЛАЙ ТАК

```python
# 1. Используй пакеты для больших проектов
from converters import feet_to_meters

# 2. Импортируй только что нужно
from utils import helper

# 3. Используй __init__.py для собирания импортов
# todos/__init__.py
from .functions import get_todos

# 4. Оборачивай тестовый код в if __name__
if __name__ == "__main__":
    test_function()

# 5. Импортируй из того файла, где это определено
from .filesChecker import ensure_file_exists
```

### ❌ НЕ ДЕЛАЙ ТАК

```python
# 1. Не используй import * (неясно откуда что)
from module import *

# 2. Не создавай циклические импорты
# A.py → B.py → A.py ❌

# 3. Не импортируй из неправильного места
from todos import ensure_file_exists  # Если оно в filesChecker

# 4. Не выполняй весь код в модуле
print("Это выполнится при импорте!")  # Без if __name__

# 5. Не используй абсолютные импорты внутри пакета
# Вместо:
from todos.functions import get_todos
# Используй:
from .functions import get_todos
```

---

## 🎨 ПОЛНЫЙ ПРИМЕР ПРОЕКТА

### Структура

```
TODO_App/
├── main.py
└── todos/
    ├── __init__.py
    ├── todosFunctions.py
    └── filesChecker.py
```

### `todos/filesChecker.py`

```python
import os

def ensure_file_exists(filepath='../txtFiles/todos.txt'):
    if not os.path.exists(filepath):
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(filepath, 'w') as file:
            pass
```

### `todos/todosFunctions.py`

```python
from .filesChecker import ensure_file_exists

def get_todos(filepath='../txtFiles/todos.txt') -> list:
    ensure_file_exists(filepath)
    with open(filepath, 'r') as file:
        return file.readlines()

def write_todos(todos, filepath='../txtFiles/todos.txt'):
    ensure_file_exists(filepath)
    with open(filepath, 'w') as file:
        file.writelines(todos)

if __name__ == "__main__":
    print("Тестирую")
    todos = get_todos()
    print(todos)
```

### `todos/__init__.py`

```python
from .todosFunctions import get_todos, write_todos
from .filesChecker import ensure_file_exists
```

### `main.py`

```python
from todos import get_todos, write_todos, ensure_file_exists

def main():
    print("=== TODO App ===")
    todos = get_todos()
    todos.append("Новое задание\n")
    write_todos(todos)
    print("✅ Готово!")

if __name__ == "__main__":
    main()
```

### Запуск

```bash
python main.py
# Или
python TODO_App/main.py
```

---

## 🚀 БЫСТРАЯ СПРАВКА

| Что нужно | Синтаксис | Пример |
|-----------|-----------|--------|
| Импортировать модуль | `import X` | `import os` |
| Импортировать функцию | `from X import Y` | `from os import path` |
| Переименовать | `import X as Y` | `import numpy as np` |
| Из папки (пакета) | `from . import X` | `from .functions import get` |
| Собрать импорты | В `__init__.py` | `from .module import func` |
| Только при запуске | `if __name__ == "__main__":` | Тестовый код |
| Избежать цикла | Импортировать из модуля | `from .files import func` |

---

## 💡 БЫСТРЫЕ ОТВЕТЫ

**Вопрос:** Файл это модуль?
**Ответ:** Да! `functions.py` это модуль `functions`

**Вопрос:** Папка это пакет?
**Ответ:** Да, если в ней есть `__init__.py`

**Вопрос:** Почему `__init__.py` важна?
**Ответ:** Без неё Python не видит папку как пакет

**Вопрос:** Что выполнится при импорте?
**Ответ:** ВСЕ, кроме `if __name__ == "__main__":`

**Вопрос:** Как избежать циклического импорта?
**Ответ:** Импортируй из того файла, где это определено

**Вопрос:** Класс это функция?
**Ответ:** Нет! Класс это шаблон, нужно создать объект

**Вопрос:** Функция это класс?
**Ответ:** Нет! Функция это действие, можешь вызвать сразу

---

**Создано:** Шпаргалка по Python импортам и модулям
**Версия:** 1.0
