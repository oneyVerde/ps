import sys
input = sys.stdin.readline

num, share = map(int, input().split())
house = []
for _ in range(num):
    house.append(int(input()))
house.sort()

start = 0
end = house[-1]
ans = 0

while start <= end:
    mini = (start + end) // 2

    curr = house[0]
    count = 1

    for i in range(1, num):
        val = house[i]

        if curr + mini <= val:
            count += 1
            curr = val
        
    if count >= share:
        start = mini + 1
        ans = mini
    else:
        end = mini - 1
    

print(ans)