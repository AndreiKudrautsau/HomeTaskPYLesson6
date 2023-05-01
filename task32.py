# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
numberMin = int(input("Enter the minimum number: "))
numberMax = int(input("Enter the maximum number: "))
lstInd = []
for i in range (len(lst)):
    if lst [i] >= numberMin and lst [i] <= numberMax:
        lstInd.append(i)
print (lstInd)
