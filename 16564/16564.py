N, K = map(int, input().split())
Tmin = 0

lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()

start = min(lst)            # 가장 작은 값부터 시작
end = start + K             # max 경우까지 생각

while start <= end:
    mid = (start + end) // 2

    # 필요한 레벨
    need_level = 0
    for l in lst:
        # mid 값이 현재 레벨보다 크다면
        if mid > l:
            need_level = need_level + (mid - l)

    # 더 팀레벨 올리기
    if K >= need_level:
        Tmin = mid
        start = mid + 1
    # 팀레벨 낮추기
    else:
        end = mid - 1

print(Tmin)