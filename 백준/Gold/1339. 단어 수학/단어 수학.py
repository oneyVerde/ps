import sys
input = sys.stdin.readline

n = int(input())

ls = [[0]*8 for _ in range(26)]
total = [0 for _ in range(26)]
while n:
    n -= 1
    val = input().strip()
    for i in range(len(val)):
        ls[ord(val[i])-65][len(val)-i-1] += 1
for i in range(26):
    for j in range(8):
        total[i] += ls[i][j] * (10**j)
total.sort(reverse=True)
for i in range(10):
    total[i] *= 9-i
print(sum(total))