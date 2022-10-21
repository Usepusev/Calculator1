#Модуль арифметики
from math import *

def check(s1, s2):   #проверка на целое число
    try:
        float(s1)
        a = True
    except ValueError:
        return False

    try:
        float(s2)
        return True
    except ValueError:
        return False

def sum(x, y): # функция сложени
    if check(x, y):
      return float(x)+float(y)
    else:
      return("o1")
def minus(x, y): # функция вычетания 
    if check(x, y):
      return float(x)-float(y)
    else:
      return("o1")
def mnog(x, y): # Функция умножения
    if check(x, y):
      return float(x)*float(y)
    else:
      return("o1")
def delenie(x, y): # Функция деления 
    if check(x, y):
        if int(y) == 0: # проверка на деление на ноль
            return("o2")
        else:
            return float(x)/float(y)
    else:
        return("o1")


def perevod(number):
    k=0
    for i in number:
        if i in "01":
            k+=1
    if k!=len(number): # Проверка на двоичное число
        return("o1")
    else:
        dec_number= int(number, 2) # перевод в 10ю систему
        oct_number= (oct(int(number, 2))).replace("0o", "")# перевод в 8ю систему
        hex_number= (hex(int(number, 2))).replace("0x", "") # перевод в 16ю систему
        l = f'10:{dec_number}\n8:{oct_number}\n16:{hex_number}' #структура вывода
        return l 
# переписал функцию check