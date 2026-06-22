

def get_average():
    with open("../files/data.txt") as f:
        data = f.readlines()

        values = data[1:]
        values = [float(i) for i in values]
        average_local = sum(values) / len(values)

    return average_local


average = get_average()
print(average)



######################## ######################## ########################

def greet(message):
    return message.capitalize() + "!"

user_entry = input("greeting somehow here: ")
greeting = greet(user_entry)

print(greeting)