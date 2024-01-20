from collections import deque
N = int(input())

graph = []

for _ in range(N):
    lst = list(input())
    graph.append(lst)

visited = [[False] * N for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 있는 경우
        if 0 <= nx < N and 0 <= ny < N:
            # 방문하지 않았고, 그 전 노드와 지금 노드와 같을 때 실행
            if visited[nx][ny] == False and graph[nx][ny] == graph[x][y]:
                # 방문함으로 변경
                visited[nx][ny] = True
                dfs(nx, ny)

cnt1 = 0
cnt2 = 0

# 적록생맹 아닌(=정상) 인 경우
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            cnt1 = cnt1 + 1

# 적록색맹인 사람 구역 수 구하기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R' #이부분!

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i, j)
            cnt2 = cnt2 + 1

print(cnt1, cnt2)