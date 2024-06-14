print("Введите натуральное число: ")
num = int(input())

count = 0

if num < 0:
    print("Вы ввели НЕ натуральное число")
else:
    for i in range(0, num):
        if i != 0 and num % i == 0:
            count += 1

print("Количество натуральных делителей у введенного числа: " + str(count))