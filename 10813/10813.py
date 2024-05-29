N, M = map(int, input().split())

lst = []

bascket = list(range(1, N+1))

for i in range(M):
    lst.append(list(map(int, input().split())))

for i in range(M):
    r, c = lst[i]
    bascket[r-1], bascket[c-1] = bascket[c-1], bascket[r-1]

for ball in bascket:
    print(ball, end=' ')