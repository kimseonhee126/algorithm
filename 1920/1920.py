N = int(input())
lst1 = list(map(int, input().split()))

M = int(input())
lst2 = list(map(int, input().split()))

lst1.sort()

def binary(lst, start, end, key):
    while start <= end:
        mid = (start+end) // 2

        if lst[mid] == key:
            return True
        elif lst[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    return False

for i in range(M):
    b = binary(lst1, 0, N-1, lst2[i])
    if b == True:
        print(1)
    else:
        print(0)