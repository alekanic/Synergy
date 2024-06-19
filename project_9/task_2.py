import collections

# Эта функция будет создавать новую запись с информацией о питомце и добавлять
# эту информацию в словарь pets
def create():
    last = collections.deque(pets, maxlen=1)[0]
    print("Введите имя питомца:")
    name = input()
    print("Введите вид питомца:")
    species = input()
    print("Введите возраст питомца:")
    age = int(input())
    print("Введите имя владельца:")
    owner = input()
    pets[last + 1] = {name : {"Вид питомца" : species, "Возраст питомца" : age, "Имя владельца" : owner}}
    print("Информация о питомце успешно добавлена!")

# Данная функция будет отображать информацию о запрашиваемом питомце в виде:
# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша.
def read():
    print("Введите идентификатор питомца: ")
    ID = int(input())
    if ID in pets.keys():
        name = list(pets[ID].keys())
        suffix = get_suffix(pets[ID][name[0]]["Возраст питомца"])
        print("Это " + (pets[ID][name[0]]["Вид питомца"]).lower() + " по кличке \""+ name[0] + "\". ", end='')
        print("Возраст питомца: " + str(pets[ID][name[0]]["Возраст питомца"]) + suffix, end='')
        print(". Имя владельца: " + pets[ID][name[0]]["Имя владельца"] + ".")
    else:
        print("Питомца с таким идентификатором нет")

# Данная функция будет обновлять информацию об указанном питомце
def update():
    print("Введите идентификатор питомца: ")
    ID = int(input())
    if ID in pets.keys():
        print("Текущая информация по питомцу: ")
        print(get_pet(ID))
        print("Что вы хотите обновить?")
        print("1 - имя питомца")
        print("2 - возраст питомца")
        print("3 - имя владельца")
        print("4 - вид питомца")
        number = int(input())
        # Берем кличку
        tmp_list = list(pets[ID].keys())
        old_key = tmp_list[0]
        if number == 1:
            print("Введите актуальное имя питомца:")
            tmp = input()
            old_value = pets[ID].pop(old_key)
            new_key = tmp
            pets[ID][new_key] = old_value
        elif number == 2:
            print("Введите актуальный возраст питомца:")
            tmp = int(input())
            pets[ID][old_key]["Возраст питомца"] = tmp
        elif number == 3:
            print("Введите актуальное имя владельца:")
            tmp = input()
            pets[ID][old_key]["Имя владельца"] = tmp
        elif number == 4:
            print("Введите актуальный вид питомца:")
            tmp = input()
            pets[ID][old_key]["Вид питомца"] = tmp
    else:
        print("Питомца с таким идентификатором нет")

# Данная функция будет удалять запись о существующем питомце
def delete():
    print("Введите идентификатор питомца, которого вы хотите удалить:")
    ID = int(input())
    if ID in pets.keys():
        del pets[ID]
        print("Удаление информации о питомце с идентификатором " + str(ID) + "прошло успешно")
    else:
        print("Питомца с таким идентификатором нет в базе")

# Функция, с помощью которой вы получите информацию о питомце в виде словаря
# Сделайте проверку, если питомца с таким ID нету в нашей БД
# Верните в этом случае FALSE
# А если питомец все же есть в БД, верните информацию о нем

def get_pet(ID):
    if ID in pets.keys():
        return pets[ID]
    else:
        print("Такого питомца нет")
        return False

# Функция, с помощью которой можно получить суффикс
# год / года / лет
# Функция будет возвращать соответствующую строку
def get_suffix(age):
    tmp = " лет"
    if age % 10 == 1:
        tmp = " год"
    elif age >= 2 and age <= 4:
        tmp = " года"
    elif age > 20 and age % 10 >= 2 and age % 10 <= 4:
        tmp = " года"
    return tmp

# Эта функция будет создана для удобства отображения всего списка питомцев
# Информацию по каждому питомцу можно вывести с помощью цикла for

def pets_list():
    for i in pets:
        print(get_pet(i))

def print_menu():
    print("create - чтобы создать новую запись")
    print("read - чтобы отобразить информацию о конкретном питомце")
    print("update - чтобы обновить информацию о конкретном питомце")
    print("delete - чтобы удалить запись о существующем питомце")
    print("list - чтобы отобразить информацию по всем животным")

pets = {
    1: {
        "Мухтар": {
            "Вид питомца" : "Собака",
            "Возраст питомца" : 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца" : "желторотый питон",
            "Возраст питомца" : 19,
            "Имя владельца" : "Саша"
        },
    }
}

# ==============================
# Основная часть программы
# ==============================

print_menu()
command = input()

while (command != 'stop'):

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "menu":
        print_menu()
    elif command == "list":
        pets_list()

    print("Введите следующую команду:")
    command = input()