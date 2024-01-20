from collections import deque
N, M = int(input().split())

graph = []

for i in range(N):
    lst = list(map(int, input().split()))
    graph.append(lst)

copy_graph = graph.copy()

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs():
    q = deque()

    # 2가 감염시킬 수 있는 모든 곳을 알아본다
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 2:
                q.append([i, j])
    
    # 만약 범위 안에 있는 값이 0이라면 2로 변환
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                continue
            if copy_graph[nx][ny] == 0:
                q.append([nx, ny])
                copy_graph[nx][ny] == 2

    result = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 0:
                cnt = cnt + 1
    # 2가 가장 많이 감염시킬 수 있을 때까지 감염
    result = max(cnt, result)