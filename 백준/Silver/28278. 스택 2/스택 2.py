import sys
input = sys.stdin.readline

def is_int(num):
    if num % 2== 0 or num % 2 == 1:
        return True
    else:
        return False


n = int(input())
ls = []
while n:
    n -= 1
    v = list(map(int, input().split()))
    if v[0] == 1:
        if is_int(v[1]):
            ls.append(v[1])
    elif v[0] == 2:
        if len(ls) > 0:
            print(ls[-1])
            del ls[-1]
        else:
            print(-1)
    elif v[0] == 3:
        print(len(ls))
    elif v[0] == 4:
        if len(ls) > 0:
            print(0)
        else:
            print(1)
    else:
        if len(ls) > 0:
            print(ls[-1])
        else:
            print(-1)