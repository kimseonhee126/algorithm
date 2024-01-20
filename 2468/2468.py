from collections import deque
import sys
sys.setrecursionlimit(100000)


N = int(input())

graph = []
q = deque()

for i in range(N):
    lst = list(map(int, input().split()))
    graph.append(lst)

max_height = max(max(graph))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dfs(x, y, h):
    # dx, dy 활용해서 십자가 탐색
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # nx, ny가 행렬 범위 안에 있고,
        # visited[nx][ny]가 아직 방문하지 않았고,
        # 해당 위치가 물에 잠기지 않는 위치라면
        if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and graph[nx][ny] > h:
            visited[nx][ny] = True
            dfs(nx, ny, h)


h = 1
cnt = 1
while h <= max_height:
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    # 비 안 온 영역 흰색으로 만들기
    for x in range(N):
        for y in range(N):
            if graph[x][y] >= h and not visited[x][y]:
                h = h + 1
                cnt = cnt + 1
                visited[x][y] = True
                dfs(x, y, h)

print(cnt)