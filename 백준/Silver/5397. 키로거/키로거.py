import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    string = list(input().strip())
    length = len(string)
    left, right = [], []

    for s in string:
        if s == '<':
            if left:
                right.append(left.pop())
        elif s == '>':
            if right:
                left.append(right.pop())
        elif s == '-':
            if left:
                left.pop()
        else:
            left.append(s)

    left.extend(reversed(right))

    print(''.join(left))