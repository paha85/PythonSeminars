list_1 = [1, 12, 6, 7, 8, 15]
k = 11
j = 0

for i in list_1:
    if i > j:
        j = i
        if j >= k:
            break

print(j)