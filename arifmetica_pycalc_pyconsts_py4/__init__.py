import Arifmetica
import calc
import consts
import degrees_n_fact
#import oct_perevod
#import perevodF10

signal = 0
#o1 = not num
#o2 = del 0
#o3 = ООП
#o4 = not num or < 0

while True:
    result = None
    command = input("Введите команду: ")
    if command == "sum":
        while True:
            a, b = map(str, input("Введите 2 неотрицательных числа: ").split())

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())
            if b == "pi":
                b = str(consts.const_pi())
            if b == "e":
                b = str(consts.const_e())

            result = Arifmetica.sum(a, b)
            if result == "o1":
                print("Введено не число, повторите ввод")
            else:
                break
        
    if command == "minus":
        while True:
            a, b = map(str, input("Введите 2 неотрицательных числа: ").split())

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())
            if b == "pi":
                b = str(consts.const_pi())
            if b == "e":
                b = str(consts.const_e())

            result = Arifmetica.minus(a, b)
            if result == "o1":
                print("Введено не число, повторите ввод")
            else:
                break

    if command == "mnog":
        while True:
            a, b = map(str, input("Введите 2 неотрицательных числа: ").split())

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())
            if b == "pi":
                b = str(consts.const_pi())
            if b == "e":
                b = str(consts.const_e())

            result = Arifmetica.mnog(a, b)
            if result == "o1":
                print("Введено не число, повторите ввод")
            else:
                break

    if command == "delenie":
        while True:
            a, b = map(str, input("Введите 2 неотрицательных числа: ").split())

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())
            if b == "pi":
                b = str(consts.const_pi())
            if b == "e":
                b = str(consts.const_e())

            result = Arifmetica.delenie(a, b)
            if result == "o1":
                print("Введено не число, повторите ввод")
            elif result == "o2":
                print("Деление на 0, повторите ввод")
            else:
                break

    if command == "perevod":
        while True:
            a = input("Введите двоичное неотрицательное число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            result = Arifmetica.perevod(a)
            if result == "o1":
                print("Введено не число, повторите ввод")
            else:
                break

    if command == "msin":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())
            
            result = calc.msin(a)
            if result == "o1":
                print("Введено не число, повторите ввод")
            else:
                break

    if command == "mcos":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            result = calc.mcos(a)
            if result == "o1":
                print("Введено не число, повторите ввод")
            else:
                break

    if command == "mtg":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            result = calc.mtg(a)
            if result == "o1":
                print("Введено не число, повторите ввод")
            elif result == "o2":
                print("Деление на 0, повторите ввод")
            else:
                break

    if command == "mctg":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            result = calc.mctg(a)
            if result == "o1":
                print("Введено не число, повторите ввод")
            elif result == "o2":
                print("Деление на 0, повторите ввод")
            else:
                break

    if command == "masin":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            result = calc.masin(a)
            if result == "o1":
                print("Введено не число, повторите ввод")
            elif result == "o3":
                print("Ошибка области определения")
            else:
                break

    if command == "macos":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            result = calc.macos(a)
            if result == "o1":
                print("Введено не число, повторите ввод")
            elif result == "o3":
                print("Ошибка области определения")
            else:
                break

    if command == "matg":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            result = calc.matg(a)
            if result == "o1":
                print("Введено не число, повторите ввод")
            else:
                break

    if command == "mactg":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            result = calc.mactg(a)
            if result == "o1":
                print("Введено не число, повторите ввод")
            else:
                break

    if command == "bi":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            if calc.isint(a) == True:
                result = calc.hex_to_bi(a)
                break
            else:
                print("Введено не число, повторите ввод")

    if command == "dec":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            if calc.isint(a) == True:
                result = calc.hex_to_dec(a)
                break
            else:
                print("Введено не число, повторите ввод")

    if command == "oct":
        while True:
            a = input("Введите число:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

            if calc.isint(a) == True:
                result = calc.hex_to_oct(a)
                break
            else:
                print("Введено не число, повторите ввод")
    
    if command == "stepen":
        while True:
            a = input("Введите число ,которое хотите возвести в степень:  ")

            if a == "pi":
                a = str(consts.const_pi())
            if a == "e":
                a = str(consts.const_e())

    if command == "exit":
        break
    elif command not in ["oct","dec","bi","mactg","matg","macos","masin","mctg","mtg","msin","mcos","perevod","delenie","mnog","minus","sum","","","","","","","","",""]:
        print("Введена неверная команда, повторите ввод")
        continue
    print(result)