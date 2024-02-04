n, k = map(int, input().split())

lst = [[1] for _ in range(n+1)]

lst[0] = [1]
lst[1] = [1, 1]

for i in range(2, n+1):
    temp = []
    for j in range(0, i+1):
        if j == 0 or j == i:
            temp.append(1)
        else:
            temp.append(lst[i-1][j-1] + lst[i-1][j])
    lst[i] = temp

print(lst[n-1][k-1])