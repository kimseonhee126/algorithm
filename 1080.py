import sys
N, M = map(int, sys.stdin.readline().split())

A = []
for i in range(N):
    A.append(list(map(int, input())))

B = []
for i in range(N):
    B.append(list(map(int, input())))

for i in range(M):
    for j in range(3):
        A[i][j] B[i][j]