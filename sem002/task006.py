s = 8
p = 16

a = list(range(2, 1000))
b = list(range(2, 1000))

for i in a:
    for j in b:
        if i * j == p and i + j == s:
            if j >= i:
                print(i, j)
