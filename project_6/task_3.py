import math

print("Введите максимальный вес, который лодка способна выдержать: ")
max_weight = float(input())
print("Введите количество рыбаков (вам потом их вес вводить по-отдельности): ")
fisherman = int(input())

common_weight = 0

for i in range(fisherman):
    print("Введите вес следующего рыбака: ")
    weight = float(input())
    if (weight > max_weight):
        print("Этого рыбака никакая лодка не выдержит, он своим ходом добирается")
    else:
        common_weight += weight

divide_by_weight = math.ceil(common_weight / max_weight)
divide_by_count = math.ceil(fisherman / 2)
if divide_by_weight > divide_by_count:
    count_of_boats = divide_by_weight
else:
    count_of_boats = divide_by_count

print("Количество рыбаков: " + str(fisherman) + ". В лодку помещаются максимум 2 человека.")
print("Общий вес рыбаков: " + str(common_weight) + ". А максимальный на лодку: " + str(max_weight))
print("Необходимое количество лодок: " + str(count_of_boats))

