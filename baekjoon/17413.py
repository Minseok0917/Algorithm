str = input()+" "
stack = []
size = 0
ans = ''
for char in str:
    if char == '<':
        while size:
            ans += stack.pop()
            size-=1
        stack.append(char)
        size+=1
        ans += char
    elif char == '>':
        stack.pop()
        size-=1
        ans+= char
    else:
        if size == 1 and stack[size-1] == "<":
            ans+=char
        elif char == ' ' or char == '\n':
            while size:
                ans+=stack.pop()
                size -= 1
            ans += ' '
        else:
            stack.append(char)
            size+=1

print(ans.strip())