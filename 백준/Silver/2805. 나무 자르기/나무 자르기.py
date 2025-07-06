n,need = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for t in tree:
        if t > mid:
            total += t-mid
    
    if total >= need:
        start = mid + 1
    else:
        end = mid - 1

print(end)