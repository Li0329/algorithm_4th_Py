arr = [[0 for i in range(3)] for i in range(3)]
arr[0][1] = 1
arr[1][1] = 1
arr[2][1] = 1
print(arr)
for i in range(3):
    for j in range(3):
        if arr[i][j]:
            arr[i][j] = '*'
        else:
            arr[i][j] = ' '

print(arr)