for _ in range(3):
    s = str(input())
    maxi = 1
    cnt = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            maxi = max(cnt,maxi)
            cnt = 1 
    maxi = max(cnt, maxi)
    print(maxi)