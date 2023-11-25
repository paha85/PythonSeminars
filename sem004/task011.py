var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'

print (list(map(int, var1.split())))
print (list(map(int, var2.split())))
print (list(map(int, var3.split())))

sum = list()
for i in list(map(int, var2.split())):
    if i in list(map(int, var3.split())):
        sum.append(i)
print(*sum)