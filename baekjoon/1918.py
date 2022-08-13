strs = input().strip()
dict = {
    "*":3,
    "/":3,
    "+":2,
    "-":2,
    "(":4,
}
stack = []
ans = ''

for char in strs:
    if char.isupper():
        ans+=char
    else:
        if char == ')':
            while stack:
                if stack and stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    ans+=stack.pop()
        else:
            if stack and dict[stack[-1]] > dict[char]:
                while stack:
                    if not stack[-1] == '(':
                        ans += stack.pop()
                    else:
                        break
            elif stack and dict[stack[-1]] == dict[char] and not stack[-1] == '(':
                ans += stack.pop()
            stack.append(char)
while stack:
    ans += stack.pop()

print(ans)