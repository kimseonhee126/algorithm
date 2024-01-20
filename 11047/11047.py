import sys
N, K = map(int, sys.stdin.readline().split())

coins = [0] * N
for i in range(N):
    coins[i] = int(input())

# 큰 수부터 정렬되도록(내림차순)
coins.sort(reverse=True)

# 몫 : 동전으로 나눴을 때 '개수'
# 나머지 : 더 작은 크기의 동전으로 나눠야 하는 '값'
result = 0
for i in range(len(coins)):
    result = result + (K // coins[i])
    K = K % (coins[i])

print(result)