print("Введите первый массив чисел через пробел: ")
arr_one = map(int, input().split())
print("Введите второй массив чисел через пробел: ")
arr_two = map(int, input().split())

set_one = set(arr_one)
set_two = set(arr_two)

common_elements = set_one.intersection(set_two)
count_of_common_elements = len(common_elements)

print("Количество одинаковых элементов: " + str(count_of_common_elements))