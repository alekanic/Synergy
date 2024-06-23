def count_letter(word):
    count_a = word.count('a')
    count_e = word.count('e')
    count_i = word.count('i')
    count_o = word.count('o')
    count_u = word.count('u')

    tmp_list = {'a':count_a, 'e':count_e, 'i':count_i, 'o':count_o, 'u':count_u}

    for i in tmp_list.keys():
        if tmp_list[i] == 0:
            print(f"Гласная \'{i}\': False")
        else:
            print(f"Гласная \'{i}\': встречается в слове {tmp_list[i]} раз(а)")


print("Введите слово: ")
word = input()
vowels = set("aeiou")
vowels_count = 0
consonants_count = 0

for letter in word:
    if letter in vowels:
        vowels_count += 1
    else:
        consonants_count += 1



print("Количество гласных: " + str(vowels_count))
print("Количество согласных: " + str(consonants_count))
count_letter(word)
