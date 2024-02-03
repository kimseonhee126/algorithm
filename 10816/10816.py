from bisect import bisect_left, bisect_right

N = int(input())
lst1 = list(map(int, input().split()))
lst1.sort()

M = int(input())
lst2 = list(map(int, input().split()))

def binary(lst, key):
    left_idx = bisect_left(lst, key)
    right_idx = bisect_right(lst, key)

    return right_idx - left_idx

for i in range(M):
    print(binary(lst1, lst2[i]), end=' ')