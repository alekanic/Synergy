print("Введите первое целое число: ")
one = int(input())
print("Введите второе целое число: ")
two = int(input())

if (one > two):
    print("Нарушено условие соглашения")
    print("Внимательно прочитайте условие задачи")
else:
    numbers = [str(i) for i in range (one, two + 1)]
    result = ' '.join(numbers)
    print(result)