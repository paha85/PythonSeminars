coins = [1, 1, 1, 1, 0]
zeros = 0
ones = 0

for i in coins:
    if i == 0:
        zeros+=1
    else:
        ones+=1

if zeros >= ones:
    print(ones)
else:
    print(zeros)