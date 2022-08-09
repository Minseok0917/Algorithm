import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    str = input()
    stack = []
    size = 0
    for char in str:
        if char == ' ' or char == '\n':
            while size > 0:
                print(stack.pop(),end='')
                size-=1
            print(char,end="")
        else:
            stack.append(char)
            size+=1

