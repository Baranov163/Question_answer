import random

score = 0

answer = None

questions = [
    "В каком году умер Сталин?",
    "Какая семья владеет брендом BMW?",
    "Сколько будет 300 + 300?"
]

answers = ['1954', 'Квандт', 'Три сотни']
for i in range(len(questions)):
    print(questions[i])
    answer = input()
    if answer == answers[i]:
        score += 1
        print('Верно!')
    else:
        print('Неверно!')

print("Ваш результат:", score)
