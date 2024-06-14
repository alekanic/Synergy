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