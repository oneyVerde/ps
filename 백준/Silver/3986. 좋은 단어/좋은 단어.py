n = int(input())
count = 0
for _ in range(n):
    string = input()
    length = len(string)
    stack = []
    for i in range(length):
        if stack == []:
            stack.append(string[i])
        elif stack[-1] == string[i]:
            stack.pop()
        else:
            stack.append(string[i])    
    if stack == []:
        count += 1
print(count)