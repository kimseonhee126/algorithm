S = int(input())

# 개수 카운트
cnt = 0

for i in range(1, S):
    S = S - i
    # 만약 S > i 라면 카운트 수를 +1씩 증가한다
    if (S > i):
        cnt = cnt + 1
    # 그게 아니라면 멈춘다
    else:
        break

# 마지막에서 그 전 숫자를 빼지 않으므로 카운트 수가 증가하지 않았다
# 그러므로 카운트 수를 +1 해야한다
cnt = cnt + 1
print(cnt)