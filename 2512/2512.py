N = int(input())
lst = list(map(int, input().split()))
M = int(input())

start = 0
end = max(lst)

while start <= end:
    mid = (start + end) // 2
    lst_copy = lst.copy()

    for i in range(N):
        if lst_copy[i] > mid:
            lst_copy[i] = mid
    
    if sum(lst_copy) <= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)