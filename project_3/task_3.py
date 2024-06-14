print("Какая минимальная озвученная сумма инвестиций?")
min_sum = int(input())
print("Сколько долларов у Майкла?")
Mickle = int(input())
print("Сколько долларов у Ивана?")
Ivan = int(input())

can_Mickle_invest = Mickle >= min_sum
can_Ivan_invest = Ivan >= min_sum
common_invest = Mickle + Ivan >= min_sum

if can_Ivan_invest and can_Mickle_invest:
    print(2)
elif can_Ivan_invest:
    print("Ivan")
elif can_Mickle_invest:
    print("Mike")
elif common_invest:
    print(1)
else:
    print(0)