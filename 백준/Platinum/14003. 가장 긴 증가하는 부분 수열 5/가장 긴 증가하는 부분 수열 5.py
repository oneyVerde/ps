import sys
input = sys.stdin.readline

def binary_search(target):
    start, end = 0, len(arr)-1
    
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid-1] < target < arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid-1
        else:
            start = mid+1

    return start


n = int(input())
ls = list(map(int, input().split()))
arr = [ls[0]]
res = []

for i in range(1, n):
    if arr[-1] < ls[i]:
        arr.append(ls[i])
    else:
        idx = binary_search(ls[i])
        res.append((arr[idx], idx))
        arr[idx] = ls[i]
for i in range(len(res)-1, -1, -1):
    idx = res[i][1]
    if idx != len(arr)-1:
        if res[i][0] < arr[idx+1]:
            arr[idx] = res[i][0]

print(len(arr))
print(" ".join(map(str,arr)))