import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

def pow_f(x,y):
    if y == 0:
        return 1
    else:
        res = pow_f(x, y//2)
        if y % 2 == 0:
            return (res * res) % c
        else:
            return (res * res * x) % c

print(pow_f(a,b))