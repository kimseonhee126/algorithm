from collections import deque

A, B = map(int, input().split())

q = deque()

q.append((B, 1))

while(A != B):

    B, cnt = q.popleft()

    if (B % 10 == 1):
        B = B // 10
        cnt = cnt + 1
        q.append((B, cnt))

    elif (B % 2 == 0 and B != 0):
        B = B // 2
        cnt = cnt + 1
        q.append((B, cnt))

    else:
        cnt = -1
        break

print(cnt)