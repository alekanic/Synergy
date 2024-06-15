print("Введите строку с кучей пробелов: ")
str = input()
space = ' '
count = 0
characters = []

for ch in str:
    if ch == space and count == 0:
        characters.append(ch)
        count += 1
    elif ch == space and count != 0:
        count += 1
    else:
        characters.append(ch)
        count = 0

print(''.join(characters))