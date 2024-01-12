import sys
N = int(input())
distances = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

min_price = prices[0]
sum_distance = 0

for i in range(len(distances)):
    # 만약 min_price 값이 가장 작은 값이 아니면 변경
    if min_price > prices[i]:
        min_price = prices[i]
    
    # 필요한 주유량(거리) * 가장 작은 주유값
    sum_distance = sum_distance + (min_price * distances[i])

print(sum_distance)