import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
for i in range(N+1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N+1) # dfs 방문기록
visited2 = [False] * (N+1) # bfs 방문기록

def bfs(V):
    q = deque([V])
    # V 방문
    visited2[V] = True
    while q:
        V = q.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if not visited2[i] and graph[V][i]:
                q.append(i)
                visited2[i] = True

def dfs(V):
    # V 방문
    visited1[V] = True
    print(V, end=' ')
    for i in range(1, N+1):
        if not visited1[i] and graph[V][i]:
            dfs(i)

dfs(V)
print()
bfs(V)