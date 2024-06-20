import random

def fill_the_matrix(matrix, width, height):
    for i in range(height):
        for j in range(width):
            matrix[i][j] = random.randint(-200, +200)

def sum_the_matrix(matrix_one, matrix_two, width, height):
    matrix_result = [[1 for i in range(width)] for i in range(height)]
    for i in range(width):
        for j in range(height):
            matrix_result[i][j] = matrix_one[i][j] + matrix_two[i][j]
    return matrix_result

#========================================
# Основная часть программы
#========================================

print("Введите ширину для матрицы:")
width = int(input())
print("Введите высоту для матрицы:")
height = int(input())

matrix_one = [[1 for i in range(width)] for i in range(height)]
matrix_two = [[1 for i in range(width)] for i in range(height)]

fill_the_matrix(matrix_one, width, height)
fill_the_matrix(matrix_two, width, height)
result = sum_the_matrix(matrix_one, matrix_two, width, height)

print("Первая матрица:")
for i in matrix_one:
    print(i)
print()
print("Вторая матрица:")
for i in matrix_two:
    print(i)
print()
print("Результирующая матрица:")
for i in result:
    print(i)