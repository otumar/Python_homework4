# Задача №30: Вычислить число c заданной точностью d. 

from math import pi

number = int(input("Enter your number that determines the accuracy of the calculation of PI: "))
number = round(pi, number)
print(f'The PI number with determined accuracy is: {number}')
