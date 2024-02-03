N, M = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(int(input()))

start = max(lst)
end = sum(lst)

while start <= end:
    mid = (start + end) // 2

    cnt = 1         # 횟수
    hap = mid         # 합 계산

    for i in range(len(lst)):
        if lst[i] > hap:
            cnt = cnt + 1       # 횟수 증가
            hap = mid
        hap = hap - lst[i]      # hap에서 일일 사용량 빼기
        
    if cnt <= M:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)