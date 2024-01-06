N = int(input())
p_list = list(map(int, input().split()))

# 오름차순으로 정렬
p_list.sort()

# ans : 결과 담을 배열
ans = [0] * (N+1)

# 누적 합
# 1, 1+2, 1+2+3, 1+2+3+4 ... 이런 식으로 진행된다
for i in range(1, N+1):
    for j in range(i):
        ans[i] = ans[i] + p_list[j]

# 합의 최솟값 출력
min_sum = 0
for k in range(1, N+1):
    min_sum = min_sum + ans[k]

print(min_sum)