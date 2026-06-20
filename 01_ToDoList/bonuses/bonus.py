

user_prompt = "Enter a code: "

password = input("enter password: ")

while password != "pass123":
    password = input("enter password: ")


print("password is correct!")


# todos = []
#
# while True:
#     todo = input(user_prompt)
#     capitalized = todo.capitalize()
#     todos.append(todo)
#     print("word:", capitalized)
#     print("list:", todos)





user_prompt = "enter a todo:"
todos = []


while True:
   todo = input(user_prompt)
   print(todo.title())
   print(type(todos))
   todos.append(todo)