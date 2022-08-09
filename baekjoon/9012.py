import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    str = input().strip()
    stack = 0
    for char in str:
        if char == '(':
            stack+=1
        else:
            stack-=1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')


