n = int(input())
leave_enter = dict()
for i in range(n):
    name, state = map(str, input().split())
    if state == 'enter':
        leave_enter[name] = state
    else:
        del leave_enter[name]
leave_enter = dict(sorted(leave_enter.items(), reverse=True))
for key in leave_enter.keys():
    print(key)