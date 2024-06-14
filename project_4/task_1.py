print("Введите количество чисел, которые хотите ввести: ")
count = int(input())
zero = 0

for i in range(count):
    print("Введите число " + str(i + 1) + " из " + str(count))
    num = int(input())
    if num == 0:
        zero += 1

print("Было введено " + str(zero) + " чисел, равных нулю")