from collections import deque
N = int(input())

# 8방향으로 이동할 수 있음
dx = [1, -1, -2, -2, -1, 1, 2, 2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        # 만약 현재위치가 나이트가 최종적으로 이동하고자 하는 칸이라면
        # 수행종료
        if x == end_x and y == end_y:
            print(visited[x][y] - 1)
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # nx, ny가 범위 내에 있고 visited[nx][ny]가 0이라면
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

for _ in range(N):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    bfs(start_x, start_y)