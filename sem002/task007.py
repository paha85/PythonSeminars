n=16
a = list(range(0, n))
for i in a:
    j = 2 ** i
    if j <= n:
        print(j)
    
