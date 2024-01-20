from collections import deque
N, M = map(int, input().split())

graph = []
for _ in range(N):
    lst = list(map(int, input()))
    graph.append(lst)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        # dx, dy 사용해서 상하좌우 이동할 수 있게 설정
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치 벗어나면 X
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽이므로 이동 불가
            if graph[nx][ny] == 0:
                continue

            # 벽이 아니고 1이므로 이동
            # cnt 변수를 사용해서 칸 수를 카운트 하는게 아니라
            # graph[x][y]에 +1씩 더해가며(누적하며) 계산
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
    return graph[N-1][M-1]

print(bfs(0, 0))