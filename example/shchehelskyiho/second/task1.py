'''
Користувач вводить час у форматі `hh:mm(:ss(.ms))`, де дужки позначають необов'язковість.
Напишіть функцію, що повертає кількість повних секунд, що пройшли з опівночі.
Виведіть результат.
У випадку помилкового вводу виведіть повідомлення про помилку.
'''
import re

def validator(text):
    num = input(text)
    while not bool(re.match(r'\d{2}\:\d{2}(\:\d\d(\.\d\d)?)?$', num)):
        print('Введені дані не задовольняють умову! Спробуйте ще раз.')
        num = input(text)
    return num

date = validator('Введіть час: ')

hours = (int(date[0]+date[1]))*3600
mins = (int(date[3]+date[4]))*60

if len(date) == 8:
    sec = int(date[6]+date[7])
    answer = hours + mins + sec

if len(date) == 11:
    msec = float(date[9]+date[10])
    answer = hours + mins + sec + msec

else:
    answer = hours + mins

print(answer)