S = list(input())
T = list(input())

# s_len: S의 길이
s_len = len(S) - 1

# t_len: T의 길이
t_len = len(T) - 1

for i in range(t_len, s_len, -1):
    if T[i] == 'A':
        T.pop(-1)
    elif T[i] == 'B':
        T.pop(-1)
        T.reverse()

if S == T:
    print(1)
else:
    print(0)