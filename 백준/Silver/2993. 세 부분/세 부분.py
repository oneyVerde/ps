init = input()
res = []

for i in range(len(init)-1):
    for j in range(i+1, len(init)-1):
        tmp = init[:i+1][::-1] + init[i+1:j+1][::-1] + init[j+1:][::-1]
        res.append(tmp)

res.sort()
print(res[0])