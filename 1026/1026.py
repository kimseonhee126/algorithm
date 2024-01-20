import sys
N = int(input())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# .copy() 하지 않으면 원본(B)이 변경되므로 .copy()를 해야한다.
b_copy = B.copy()

# A 정렬
A.sort()

# ans : 최소값
ans = 0

for i in range(len(B)):
    # a에는 순차적으로 작은 값이 들어간다
    a = A[i]
    # b에 가장 큰 값을 가진 인덱스를 pop한다
    b = b_copy.pop(b_copy.index(max(b_copy)))
    # b에서 가장 큰 값과 a에서 작은 값이 곱해진다
    ans = ans + (a * b)

print(ans)