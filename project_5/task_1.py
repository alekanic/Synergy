print("Введите строку: ")
str = input()
str.lower()

right = len(str) - 1
left = 0

result = True

while left < right:
    if str[left] == str[right]:
        left += 1
        right -= 1
    else:
        result = False
        left += 1
        right -= 1

if result == True:
    print("Строка является палиндромом")
    print("yes")
else:
    print("Строка не является палиндромом")
    print("no")

