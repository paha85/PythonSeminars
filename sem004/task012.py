arr = [5, 8, 6, 4, 9, 2, 7, 3]
print(arr)
number = 0
for i in arr:
    i = 0
    number = arr[i] + arr[i+1] + arr[i+2]
print(number)

arr_count = list()
for i in range(len(arr)):
       arr_count.append(arr[i-2] + arr[i-1] + arr[i])
print(max(arr_count))