n = int(input())
u = [0] * n

for i in range(n):
    u[i] = int(input())

a = []
for i in range(n):
    for j in range(n):
        a.append(u[i] + u[j])
a.sort()
u.sort()

def binary_search(b):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        mid_value = a[mid]
        if mid_value > b:
            end = mid - 1
        elif mid_value < b:
            start = mid + 1
        else:
            return True
    return False

for k in range(n-1, 0, -1):
    for c in range(k):
        if binary_search(u[k] - u[c]):
            print(u[k])
            exit()