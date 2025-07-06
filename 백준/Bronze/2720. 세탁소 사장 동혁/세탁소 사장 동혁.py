t = int(input())
coin = [25,10,5,1]
while t>0:
    val = int(input())
    last = val
    for i in range(4):
        print(int(last // coin[i]), end = ' ')
        last %= coin[i]
    t -= 1