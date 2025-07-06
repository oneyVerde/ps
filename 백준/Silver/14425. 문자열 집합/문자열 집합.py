import sys
input = sys.stdin.readline
n,m = map(int, input().split())
n_list, count = [], 0
for _ in range(n):
    n_list.append(str(input()))
for _ in range(m):
    input_val = str(input())
    if input_val in n_list:
        count += 1
print(count)