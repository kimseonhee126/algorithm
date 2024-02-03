a, b = map(int, input().split())

aList = sorted(list(set(map(int, input().split()))))
bList = list(set(map(int, input().split())))

def binary(lst, start, end, key):
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == key:
            lst.pop(mid)
            return lst
        elif lst[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return lst

for i in range(len(bList)):
    binary(aList, 0, len(aList)-1, bList[i])

if len(aList) != 0:
    print(len(aList))
    print(*sorted(aList))
else:
    print(0)