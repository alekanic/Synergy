pets = {}
print("Введите имя питомца: ")
name = input()
pets[name] = {}
print("Введите вид питомца: ")
species = input()
pets[name]["Вид питомца"] = species
print("Введите возраст питомца: ")
age = int(input())
pets[name]["Возраст питомца"] = age
tmp = " лет"
if age % 10 == 1:
    tmp = " год"
elif age >= 2 and age <= 4:
    tmp = " года"
elif age > 20 and age % 10 >= 2 and age % 10 <= 4:
    tmp = " года"
print("Введите имя владельца: ")
owner = input()
pets[name]['Имя владельца'] = owner

keys = list(pets.keys()) # Ну если очень надо не использовать переменную name
print("Это " + pets[name]["Вид питомца"] + " по кличке " + keys[0], end='')
print(". Возраст питомца: " + str(pets[name]['Возраст питомца']) + tmp, end='')
print(". Имя владельца: " + str(pets[name]['Имя владельца']))