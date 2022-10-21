from math import *  #библиотека для тригонометрии

def isint(s):   #проверка на целое число
    try:
        int(s)
        return True
    except ValueError:
        return False

#функциии тригонометрии
def msin(a):
    if not isint(a): # проверка на ввод
        return "o1" # код ошибки ввода
    else:
        return (str(sin(int(a)))) #синус числа

def mcos(a):
    if not isint(a): # проверка на ввод
        return "o1" # код ошибки ввода
    else:
        return (str(cos(int(a)))) #косинус числа

def mtg(a):
    if not isint(a): # проверка на ввод
        return "o1" # код ошибки ввода
    else:
        if cos(int(a)) == 0:
            return "o2" #ошибка деления на ноль
        else:
            return (sin(int(a))/cos(int(a))) #тангенс числа

def mctg(a):
    if not isint(a): # проверка на ввод
        return "o1" # код ошибки ввода
    else:
        if sin(int(a)) == 0:
            return "o2" #ошибка деления на ноль
        else:
            return (cos(int(a))/sin(int(a))) #котангенс числа

def masin(a):
    if not isint(a): # проверка на ввод
        return "o1" # код ошибки ввода
    else:
        if int(a) < -1 or int(a) > 1:
            return "o3" #ошибка области определения
        else:
            return (asin(int(a))) #арксинус числа

def macos(a):
    if not isint(a): # проверка на ввод
        return "o1" # код ошибки ввода
    else:
        if int(a) < -1 or int(a) > 1:
            return "o3" #ошибка области определения
        else:
            return (acos(int(a))) #арккосинус числа

def matg(a):
    if not isint(a): # проверка на ввод
        return "o1" # код ошибки ввода
    else:
        return (atan(int(a))) #арктангенс числа

def mactg(a):
    if not isint(a): # проверка на ввод
        return "o1" # код ошибки ввода
    else:
        return ((cos(int(a))/sin(int(a)))**-1) #арккотангенс

#перевод системы из шестнадцатиричной
def hex_to_bi(a):
    return(bin(int(a, 16)))#перевод из 16 в 2

def hex_to_dec(a):
    return(int(a, 16))#перевод из 16 в 8

def hex_to_oct(a):
    return(oct(int(a, 16)))#перевод из 16 в 10

#добавил проверку на число для перевода(пока не добавил)