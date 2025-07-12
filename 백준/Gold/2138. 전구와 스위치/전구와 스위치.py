import sys
input = sys.stdin.readline

INF = int(1e8)

def light(before, after):
    global n
    press = 0
    for i in range(1, n):
        if before[i-1] != after[i-1]:
            press += 1
            before[i-1], before[i] = 1-before[i-1], 1-before[i]
            if i+1 < n:
                before[i+1] = 1-before[i+1]
    if before == after:
        return press
    else:
        return INF


n = int(input())
input_light = list(map(int, input().strip()))
output_light = list(map(int, input().strip()))

in_light = input_light[:]
no_first = light(in_light, output_light)

input_light[0], input_light[1] = 1-input_light[0], 1-input_light[1]
on_first = light(input_light, output_light)

answer = min(no_first, on_first+1)

print(answer) if answer != INF else print(-1)