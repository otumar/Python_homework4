# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


mylist = list(map(int, input("Enter your numbers separated by a space: ").split()))
print(f"Your list is: {mylist}")
newlist = []
[newlist.append(i) for i in mylist if i not in newlist]
print(f"The list of non-reapiting elements is: {newlist}")
