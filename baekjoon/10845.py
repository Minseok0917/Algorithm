import sys

n = int(sys.stdin.readline())
q = []
begin, end = 0, 0

def front():
    global q, begin
    if not empty():
        return q[begin]
    else:
        return -1
def back():
    global q, end
    if not empty():
        return q[end-1]
    else:
        return -1
def size():
    global begin, end
    return end-begin
def empty():
    global begin,end
    if end == begin: return True
    else: return False
def pop():
    global q,begin
    if not empty():
        card = q[begin]
        q[begin] = 0
        begin+=1
        return card
    else:
        return -1
def push(value):
    global q, end
    q.append(value)
    end+=1

for _ in range(n):
    k = sys.stdin.readline().strip()
    if k == 'front': print(front())
    elif k == 'back': print(back())
    elif k == 'size': print(size())
    elif k == 'empty': print( 1 if empty() else 0 )
    elif k == 'pop': print(pop())
    else:
        k, value = k.split()
        push(value)
