num = list(input())
num.sort(reverse=True)
total = 0

if '0' not in num:
    print(-1)
else:
    for i in num:
        total += int(i)
    if total % 3 != 0:
        print(-1)
    else:
        print(''.join(num))