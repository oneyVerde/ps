s = input()
t = input()
for i in range(len(t)):
    if s == t:
        break
    if t[-1] == 'A':
        t = t[:-1]
        continue
    elif t[-1] == 'B':
        t = t[::-1]
        t = t[1:]

if s == t:
    print(1)
else:
    print(0)