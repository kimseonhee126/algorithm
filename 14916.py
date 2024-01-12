N = int(input())

ans_5 = 0
ans_2 = 0

# N이 0보다 크거나 같을때까지 진행
while N >= 0:
    # 5의 배수이면 5원 동전으로만 거슬러준다
    if (N % 5 == 0):
        ans_5 = ans_5 + (N // 5)
        print(ans_2 + ans_5)
        break
    # 5의 배수가 아니라면 2원 동전 +1, 총 금액 - 2 를 하여 다시 반복문을 진행한다
    else:
        N = N - 2
        ans_2 = ans_2 + 1

    if N < 0:
        print(-1)
        break
