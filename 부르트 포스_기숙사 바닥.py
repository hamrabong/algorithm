r, b = map(int, input().split())
for i in range(3, 2000):
    for j in range(3, i + 1):
        a = (i * 2) + ((j - 2) * 2)
        if a == r and (i * j) - a == b:
            print(i, j)
