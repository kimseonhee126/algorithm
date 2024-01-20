from collections import deque
N = int(input())
M = int(input())
V = 1

graph = [[False] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (N+1)

global cnt
cnt = 0

q = deque()

def dfs(V):
    visited[V] = True
    q.append(V)
    for i in range(1, N+1):
        if not visited[i] and graph[V][i]:
            dfs(i)

dfs(V)
print(len(q)-1)