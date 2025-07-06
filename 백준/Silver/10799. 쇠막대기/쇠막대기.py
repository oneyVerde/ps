stick = str(input())
input_length = len(stick)
stack = []
count = 0
for i in range(input_length):
    if stick[i] == '(':
        stack.append('(')
    else:
        if stick[i-1] == '(':
            count += len(stack) - 1
        else:
            count += 1
        stack.pop()
print(count)