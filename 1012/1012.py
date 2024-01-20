from collections import deque
T = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    for j in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)


for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    cnt = 0

    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                dfs(a, b)
                cnt = cnt + 1
    print(cnt)