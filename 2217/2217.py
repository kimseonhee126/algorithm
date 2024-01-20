import sys
N = int(input())

ropes = []
for i in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

weights = []
for i in range(1, N+1):
    weights.append(i * ropes[i-1])

print(max(weights))