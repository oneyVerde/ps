import heapq
import sys
input = sys.stdin.readline

n = int(input())
middle = int(input())

left, right = [], []
is_left = False # 두번째 값부터 추가, 짝수면 왼쪽 값을 middle로
answer = [middle]

for _ in range(n-1):
    value = int(input())

    if is_left:
        if middle < value:
            heapq.heappush(left, -middle) # middle을 left에 추가
            middle = heapq.heappushpop(right, value) # middle보다 크면 right에 저장하고 middle 갱신
        else:
            heapq.heappush(left, -value) # 아니면 left에 저장
    else:
        if middle > value:
            heapq.heappush(right, middle) # middle을 right에 추가
            middle = -heapq.heappushpop(left, -value) # middle보다 작으면 left에 저장하고 middle 갱신
        else:
            heapq.heappush(right, value) # 아니면 right에 저장

    is_left = not is_left
    answer.append(middle)

print('\n'.join(map(str, answer)))