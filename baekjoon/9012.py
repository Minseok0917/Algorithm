import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    str = input().strip()
    stack, size = [], 0
    for char in str:
        if char == '(':
            stack.append(char)
            size+=1
        else:
            if size == 0:
                size +=1
                break
            else:
                stack.pop()
                size-=1
    if size == 0:
        print('YES')
    else:
        print('NO')


