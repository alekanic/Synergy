print("Введите число: ")
number = int(input())

positive = number > 0
negative = number < 0
zero = number == 0
even = number % 2 == 0
uneven = number % 2 != 0

if zero:
    print("нулевое число")
elif positive and even:
    print("положительное четное число")
elif positive and uneven:
    print("положительное нечетное число")
elif negative and even:
    print("отрицательное четное число")
elif negative and uneven:
    print("отрицательное нечетное число")

if uneven:
    print("число не является четным")