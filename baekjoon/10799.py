str = input()

stack = []
size = 0
ans = 0
index=0
for char in str:
    if char == '(':
        stack.append(char)
        size+=1
    else:
        if str[index-1] == '(':
            ans += size-1
        else:
            ans += 1
        stack.pop()
        size-=1
    index+=1
print(ans)