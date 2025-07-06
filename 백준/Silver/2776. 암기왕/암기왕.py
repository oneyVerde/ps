t = int(input())

for k in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    m  = int(input())
    memory = list(map(int,input().split()))
    ls.sort()
    ans = []

    for i in range(m):
        key = memory[i]
        start = 0
        end = n-1

        while start <= end:
            mid = (start + end) // 2
            if key < ls[mid]:
                end = mid -1
            elif key > ls[mid]:
                start = mid + 1 
            else:
                ans.append(1)
                break
        
        if start > end:
            ans.append(0)

    for i in range(m):
        print(ans[i])