# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

elementFirst = int(input("Enter the first number: "))
difference = int(input("Enter difference: "))
numberElement = int(input("Enter the first number: "))
result = [] 
for i in range(1, numberElement + 1):
    a = elementFirst + (i - 1) * difference
    result.append(a)

print(result)