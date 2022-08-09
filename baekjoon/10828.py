import sys
input = sys.stdin.readline

array = []
size = 0

def push(value):
    global array, size
    array.append(value)
    size +=1
def empty():
    global size
    if size == 0: return False
    else: return True
def pop():
    global array, size
    if empty():
        top()
        array.pop()
        size -= 1
    else:
        print(-1)
def top():
    global array, size
    if empty():
        print(array[size - 1])
    else:
        print(-1)
def floor():
    global size
    print(size)


n = int(input())
for i in range(n):

    status = input().strip()
    if status == 'top': top()
    elif status == 'size': floor()
    elif status == 'empty':
        if empty(): print(0)
        else: print(1)
    elif status == 'pop': pop()
    else:
        s, n = status.split()
        push(n)
