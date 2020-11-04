"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def even_number
    while True:
    answer = input()
    if 'exit' in answer:
        break
    if answer != 'exit':
      c = float(answer)
      d = int(c)
      if d%2==0:
         print ("четное")
      else:
        continue    
     


# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."

print("Мы не продаём алкоголь несовершеннолетним") if age < 21 else sell_alcohol()

# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
def str_key(strng):
  return keyword.iskeyword(strng)

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
def get_type(your_var):                  
    if type(your_var) == int:    
        return 'число'                   
    elif type(your_var) == bool: 
        return 'булевый'                  
    elif type(your_var) == str:  
        return 'строка'                   
    elif type(your_var) == list: 
        return 'список'                  
    elif type(your_var) == tuple:
        return 'кортеж'  

    elif type(your_var) == float:
        return 'число'           

    elif type(your_var) == set:
        return 'множество'   

    elif type(your_var) == dict:
        return 'словарь'               
    else: 
        print("type is unknown")