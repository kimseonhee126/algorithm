from collections import deque

def bfs():
    q = deque()
    q.append([home_x, home_y])

    while q:
        x, y = q.popleft()
        # 페스티벌 - 집 or 페스티벌 - 편의점까지의 거리가
        # 1000이 안넘으면 한 번에 바로 갈 수 있음
        if abs(fes_x - x) + abs(fes_y - y) <= 1000:
            print('happy')
            return
        
        # 편의점을 들러야 한다면 집 - 편의점, 편의점 - 편의점, 편의점 - 페스티벌까지
        # 20병으로 갈 수 있는지 확인
        for i in range(len(graph)):
            distance = (abs(graph[i][0] - x) + abs(graph[i][1] - y))

            # 20병으로 갈 수 있고 아직 방문하지 않은 곳이라면
            if distance <= 1000 and not visited[i]:
                q.append([graph[i][0], graph[i][1]])
                visited[i] = True

    print('sad')
    return visited

t = int(input())

for _ in range(t):
    graph = []
    store_cnt = int(input())                        # 편의점 개수
    home_x, home_y = map(int, input().split())      # 집 좌표
    for k in range(store_cnt):                      # 편의점 좌표
        lst = list(map(int, input().split()))
        graph.append(lst)
    fes_x, fes_y = map(int, input().split())        # 페스티벌 좌표
    visited = [False for _ in range(store_cnt+1)]   # 방문 여부 판단
    bfs()
