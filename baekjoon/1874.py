n = int(input())
stack = []
size = 0
count = 0
ans = ''

while(n):
    m = int(input())
    if m > count:
        while m > count:
            size+=1
            count+=1
            ans += '+'
            stack.append(count)
        stack.pop()
        size-=1
        ans += '-'
    elif size > 0 and m <= stack[size-1]:
        while size > 0 and m <= stack[size-1]:
            size-=1
            ans += '-'
            stack.pop()
    elif m < count:
        print('NO')
        break
    n-=1
    if n == 0:
        for i in ans:
            print(i)



