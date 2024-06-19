def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result

def list_of_factorials(number):
    arr = []
    for i in range(number, 0, -1):
        arr.append(factorial(i))
    print(arr)

print("Факториал числа 3 равен: " + str(factorial(3)))
print("Список факториалов чисел от получившегося ранее факториала 6, до 1: ")
list_of_factorials(6)