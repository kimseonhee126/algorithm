N = int(input())

# ans_5 : 5kg 봉지 개수
ans_5 = 0

# ans_3 : 3kg 봉지 개수
ans_3 = 0

while True:
    # 5로만 성공
    if N % 5 == 0:
        ans_5 = ans_5 + (N // 5)
        print(ans_5 + ans_3)
        break

    # 5와 3의 조합으로 성공 & 3의 조합으로 성공
    elif N % 5 != 0:
        N = N - 3
        ans_3 = ans_3 + 1

    # 둘 다 아니라면 -1 출력
    if N < 0:
        print(-1)
        break

# N = int(input())

# # 5와 3의 조합으로 나누어 떨어질 
# if N % 5 != 0:
#     ans_5 = N // 5
#     if (ans_5 % 3 == 0):
#         ans_3 = ans_5 // 3
#         print(ans_3 + ans_5)
# elif N % 5 == 0:
#     ans_5 = N // 5
#     print(ans_5)

# if N % 3 == 0:
#     ans_3 = N // 3
# else:
#     print(-1)
