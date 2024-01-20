# 단지번호 붙이기
from collections import deque

N = int(input())

graph = []

for _ in range(N):
    lst = list(map(int, input()))
    graph.append(lst)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # nx, ny가 범위 내에 있고, 아직 방문하지 않았고, 집이 있는 곳이라면('1') 수행
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
                cnt = cnt + 1
                q.append([nx, ny])
                visited[nx][ny] = True
    return cnt

ans = []        # ans 배열 안에 결과 저장
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 집이 있는 곳이고('1'), 아직 방문하지 않은 곳이라면 수행
        if graph[i][j] == 1 and not visited[i][j]:
            temp = bfs(i, j) 
            ans.append(temp)

ans.sort()          # 오름차순으로 정렬되어야 하므로..!!
for a in ans:
    print(a)