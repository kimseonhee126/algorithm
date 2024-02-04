N = int(input())

# 최적의 경우의 수를 저장하는 테이블
d = [0] * (N+1)
d[1] = 1

for i in range(2, N+1):
    # '10' 을 제외하고 뒷 자리만 생각하면 d[i] 값은 d[i-1] + d[i-2] 개수를 더한 값고 같다
    d[i] = d[i-1] + d[i-2]

print(d[N])