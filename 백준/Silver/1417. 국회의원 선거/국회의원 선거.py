n = int(input())
first = int(input())
cand = [int(input()) for _ in range(n-1)]
cand.append(0)
count = 0
cand.sort()
max_idx = -1
while first <= cand[max_idx]:
    first += 1
    cand[max_idx] -= 1
    count += 1
    cand.sort()
print(count)