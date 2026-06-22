import json

with open("../experiments/questions.json") as file:
    content = file.read()

# Шаг 2: Конвертируем текст в Python структуру
data = json.loads(content)

print("-----------------")
print("JSON content: \n", content)
print("\n")
print("-----------------")


# Конвертировать в JSON строку
json_data = json.dumps(content)
print(json_data)

print("\n")

print("Start Quiz")
print("-----------------")


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = f"{index + 1} {result}  - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}"
    print(message)

print(score, "/", len(data))
