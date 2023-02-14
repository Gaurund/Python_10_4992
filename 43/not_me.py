arr = [1, 2, 1, 1, 2]
n = len(arr)
result = 0
for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            result += 1


print(arr)
print(result)
