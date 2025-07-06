month = ['SUN', 'MON', 'TUE','WED','THU','FRI','SAT']
end = [31,28,31,30,31,30,31,31,30,31,30,31]
x,y = map(int, input().split())
flag = sum(end[:x-1])%7
print(month[(y+ flag)%7])