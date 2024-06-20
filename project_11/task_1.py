def recursion(list, count):
    if count == len(list):
        print("Конец списка")
        return
    print(list[count])
    count += 1
    recursion(list, count)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
count = 0
recursion(my_list, count)
