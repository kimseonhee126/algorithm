N, M = map(int, input().split())

lst = []

bascket = [0] * N

for i in range(M):
    lst.append(map(int, input().split()))

for i in range(len(lst)):
    start, end, item = lst[i]
    for index in range(start, end+1):
        bascket[index-1] = item

for ball in bascket:
    print(ball, end=' ')