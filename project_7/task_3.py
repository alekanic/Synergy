print("Введите последовательность чисел через пробел: ")
tmp = list(map(int, input().split()))
arr = set()
for i in range(len(tmp)):
    if tmp[i] in arr:
        print("YES")
    else:
        print("NO")
    arr.add(tmp[i])
