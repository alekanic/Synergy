print("Введите число (количество чисел, которые вы потом будете вводить): ")
number = int(input())
arr = []
for i in range(number):
    print("Введите элемент массива")
    arr.append(input())
print("Вы ввели массив: ")
print(*arr)
arr.reverse()
print("Перевернутый массив: ")
print(*arr)