# Задача №31: Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


number = int(input("Enter your number: "))
i = 2  
mylist = []
newnumber = number
while i <= number:
    if number % i == 0:
        mylist.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Prime factors of {newnumber} are: {mylist}")
