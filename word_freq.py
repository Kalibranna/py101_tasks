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