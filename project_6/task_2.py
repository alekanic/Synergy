print("Введите число N (количество чисел в строке): ")
number = int(input())
print("Введите через пробел N чисел")
tmp = input().split()
arr = []
arr.append(tmp[-1])
for i in range(1, number - 1):
    arr.append(tmp[i + 1])
arr.append(tmp[0])
print("Массив, который вы ввели: ")
print(*tmp)
print("Измененный массив: ")
print(*arr)
