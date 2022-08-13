# A: 65 ~ Z: 90
# a: 97 ~ z:122
strs = input()
ans = ''

for char in strs:
    code = ord(char)
    if char == ' ':
        ans += char
    elif 65 <= code and code <= 90:
        if 65 > code-13:
            ans+=chr(91-(65-(code-13)))
        else:
            ans+=chr(code-13)
    elif 97 <= code and code <= 122:
        if 97 > code-13:
            ans+=chr(123-(97-(code-13)))
        else:
            ans+=chr(code-13)
    else:
        ans+=char


print(ans)