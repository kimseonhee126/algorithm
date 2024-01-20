# graph = [[],      # 0
#     [2, 3],  # 1 
#     [4, 5],  # 2
#     [6],     # 3
#     [2, 5],  # 4
#     [2, 4],  # 5
#     [3, 7],  # 6
#     [6]]

# visited = [False] * len(graph)

# def dfs(v):
#     visited[v] = True
#     print(v, end = ' ')

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)
# dfs(1)
# ---------------------------------------------------------------

from collections import deque

graph = [
    [],      # 0
    [2, 3],  # 1 
    [4, 5],  # 2
    [6],     # 3
    [2, 5],  # 4
    [2, 4],  # 5
    [3, 7],  # 6
    [6]      # 7
]

visited = [False] * len(graph)

def bfs(v):
    q = deque()
    # q에 시작 노드 삽입
    q.append(v)

    while q:
        x = q.popleft()
        print('node : ', x)
        for i in graph[x]:
            print('옆에 노드 : ', i)
            if not visited[i]:
                q.append(i)
                visited[i] = True
                print('현재 q : ', q)
        print('visited : ', visited)
        print()

bfs(1)