N = int(input())

lst = [[1] * 10] * N

for i in range(1, N):
    temp = []
    for j in range(10):
        if j == 0:
            temp.append(1)
        else:
            temp.append(lst[i-1][j] + temp[j-1])
    lst[i] = temp

print(sum(lst[N-1]) % 10007)