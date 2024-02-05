N = int(input())

d = [0] * (N+1)

if N >= 1:
    d[1] = 3

if N >= 2:
    d[2] = 7

# 우연히 발견한 점화식 나이스~!
for i in range(3, N+1):
    d[i] = (2 * d[i-1] + d[i-2]) % 9901

print(d[N])