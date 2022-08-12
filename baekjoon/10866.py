import sys
n = int(input())
d = []


def empty():
    global d
    if not d: return True
    else: return False

for _ in range(n):
    char = sys.stdin.readline().strip()
    if char == 'front':
        if empty(): print(-1)
        else: print(d[0])

    elif char == 'back':
        if empty(): print(-1)
        else: print(d[-1])
    elif char == 'size':
        print(len(d))
    elif char == 'empty':
        if empty(): print(1)
        else: print(0)
    elif char == 'pop_front':
        if empty():
            print(-1)
        else:
            print(d.pop(0))
    elif char == 'pop_back':
        if empty():
            print(-1)
        else:
            print(d.pop())
    else:
        s, value = char.split()
        if s == 'push_front':
            d.insert(0,value)
        elif s == 'push_back':
            d.append(value)
