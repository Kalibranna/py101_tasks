"""
Программа выводит на экран числа от 1 до 100 включительно, с новой строки.

Если число кратно трём, то вместо этого числа программа выводит слово "zip"
Если чисто кратно пяти, то вместо этого числа выводится слово "zap"
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap"

Тебе может понадобиться цикл for и ветвления
"""
number=0
for number in range(1, 15 + 1):
    if number%3 == 0  and number%15 != 0:
        print ("zip")
        number+=1
        continue
    if number%5 == 0 and number%15 != 0:
        print ("zap")
        number+=1
        continue
    if number%15 == 0 and number%3 == 0 and number%5 == 0:
        print ("zip-zap")
        number+=1
        continue
    else:
         print (number)
         number+=1