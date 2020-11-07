"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

if __name__ == '__main__':
    pass


import sys
import argparse 
import nltk
import collections
nltk.download('stopwords')
from nltk.corpus import stopwords
import os

text_dok = input("Введите путь к файлу: ")
if os.path.exists(text_dok):
    print("Указанный файл существует") 
else:
    print("Файл не существует") 
 
#открыли файл
document_text = open(check_file, 'r')
text_string = document_text.read()
text_string = document_text.read().lower()
#нашли стоп-слова
en_stops = set(stopwords.words('english'))

#отфильтровали
filtered_words = [word for word in text_string if word not in stopwords.words('english')]

frequency = {}
#посчитали
for word in filtered_words: 
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print (words, frequency[words])
  