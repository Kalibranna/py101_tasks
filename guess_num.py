"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""
import random
number_question = random.randint(1, 1000000)
number = None
while True:
    number = int(input("Введите число: "))
    if number_question == number:
        print("Победа")
        
    elif number_question < number:
        print("введите число меньше")
    elif number_question > number:
        print("введите число больше")   