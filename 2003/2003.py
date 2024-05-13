N, M = map(int, input().split())

lst = list(map(int, input().split()))

cnt = 0

left = 0
right = 1

while(right <= N and left <= right):
    calList = lst[left:right]

    if (sum(calList) == M):
        cnt = cnt + 1

        right = right + 1
    
    elif (sum(calList) < M):
        right = right + 1

    else:
        left = left + 1

print(cnt)
