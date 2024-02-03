a, b = map(int, input().split())

aSet = set(map(int, input().split()))
bSet = set(map(int, input().split()))

ans = list(aSet - bSet)

if len(ans) != 0:
    print(len(ans))
    print(*sorted(ans))
else:
    print(len(ans))