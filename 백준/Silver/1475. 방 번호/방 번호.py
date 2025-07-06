ls = [0 for _ in range(10)]
s = str(input())
for i in range(len(s)):
    val = int(s[i])
    if val == 6 or val == 9:
        if ls[6] <= ls[9]:
            ls[6] += 1
        else:
            ls[9] += 1
    else:
        ls[val] += 1
print(max(ls))