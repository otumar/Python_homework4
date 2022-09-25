# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Введите натуральную степень k = "))

def write_file(str):
    with open('myfile.txt', 'w') as data:
        data.write(str)

def rnd():
    return random.randint(0, 101)

def create_mn(p):
    mylist = [rnd() for i in range(p+1)]
    return mylist

def create_str(tr):
    mylist = tr[::-1]
    uk = ''
    if len(mylist) < 1:
        uk = 'x = 0'
    else:
        for i in range(len(mylist)):
            if i != len(mylist) - 1 and mylist[i] != 0 and i != len(mylist) - 2:
                uk += f'{mylist[i]}x^{len(mylist)-i-1}'
                if mylist[i+1] != 0:
                    uk += ' + '
            elif i == len(mylist) - 2 and mylist[i] != 0:
                uk += f'{mylist[i]}x'
                if mylist[i+1] != 0:
                    uk += ' + '
            elif i == len(mylist) - 1 and mylist[i] != 0:
                uk += f'{mylist[i]} = 0'
            elif i == len(mylist) - 1 and mylist[i] == 0:
                uk += ' = 0'
    return uk

coeff = create_mn(k)
write_file(create_str(coeff))
