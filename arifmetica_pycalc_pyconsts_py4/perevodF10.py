def perevod_10_v_2(n): #ввод функции
    if int(n)>0:     #условие целое положительное число
        b = '' #ввод переменной
        while n > 0: #цикл пока число больше 0
            b = b + str(n % 2) #сумма переменной и остатка
            n = n // 2 #деление без остатка
    else: #иначе
        b = 'ошибка 1' #вывод сообщения    
    return b #возвращение переменной

def perevod_10_v_8(n): #ввод функции
    if int(n)>0:  #условие целое положительное число
        b = '' #ввод переменной
        while n > 0: #цикл пока число больше 0
            b = str(n % 8) + b #сумма переменной и остатка
            n = n // 8 #деление без остатка
    else: #иначе
        b ='ошибка 1' #вывод сообщения 
    return b #возвращение переменной

def perevod_10_v_16(n): #ввод функции
    if int(n)>0:   #условие целое положительное число
        b = '' #ввод переменной
        h = '0123456789ABCDEF' #присваивание переменной массива
        while n > 0: #цикл пока число больше 0
            b = h[n % 16] + b #сумма переменной и остатка в соответствии с номером
            n = n // 16  #деление без остатка
    else: #иначе
        b = 'ошибка 1' #вывод сообщения 
    return b #возвращение переменной