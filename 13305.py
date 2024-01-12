import sys
N = int(input())
distances = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

pay = 0
i = 0
while i < N - 1:
    # 주유비 > 거리
    if prices[i] > (distances[i]):
        pay = pay + (prices[i] * distances[i])
        i = i + 1
    
    # 주유비 < 거리
    else:
        # 현재 주유비와 다음 주유비 비교
        # 현재 주유비 > 다음 주유비
        if prices[i] >= prices[i+1]:
            pay = pay + (prices[i] * distances[i])
            i = i + 1
        
        # 다음 주유비 > 현재 주유비
        else:
            # 다음 도로까지의 길이 더하려고
            temp = distances[i]
            for j in range(i, len(prices)):
                if prices[j+1] > prices[j]:
                    temp = temp + distances[j+1]
                else:
                    pay = pay + (temp * prices[i])
                    i = i + j
                    break

print(pay)