print("Введите пятизначное целое число: ")
number = int(input())

five = number % 10 # получим единицы
four = (number % 100 - five) // 10 # получим десятки
three = (number % 1000 - four) // 100 # получим сотни
two = (number % 10000 - three) // 1000 # получим тысячи
one =  (number - two) // 10000

result = ((four ** five) * three) / (one - two)

print(result)