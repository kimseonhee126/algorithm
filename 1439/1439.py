lst = list(input())

cnt0 = 0
cnt1 = 0

for i in range(len(lst)-1):
    if(lst[i] == '0'):
        if(lst[i] == lst[i+1]):
            continue
        else:
            cnt0 = cnt0 + 1
    else:
        if(lst[i] == lst[i+1]):
            continue
        else:
            cnt1 = cnt1 + 1

print(min(cnt0, cnt1))