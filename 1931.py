import sys
N = int(input())

times = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    times.append([a, b])

# 첫 번째: 끝나는 시간을 기준으로 오름차순으로 정렬
# 두 번째: 시작하는 시간을 기준으로 오름차순으로 정렬
# 왜 이렇게 해야하는가?
# (5 5), (3 5) 이런식으로 입력이 되면 2번으로 나와야 하는데 1번으로 나온다
times.sort(key=lambda x:(x[1], x[0]))

end_time = times[0][1]

cnt = 1
for i in range(1, N):
    if times[i][0] >= end_time:
        cnt = cnt + 1
        end_time = times[i][1]

print(cnt)