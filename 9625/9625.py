K = int(input())

# 최적의 경우를 담은 리스트
dA = [0] * (K+1)
dB = [0] * (K+1)

dA[0] = 1
dB[0] = 0

dA[1] = 0
dB[1] = 1

for i in range(2, K+1):
    dA[i] = dA[i-1] + dA[i-2]
    dB[i] = dB[i-1] + dB[i-2]

print(dA[-1], dB[-1])