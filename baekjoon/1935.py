# A: 65 ~ Z: 90
n = int(input())
m = list(input())
dict = {}
for i in range(n):
    uni = chr(i+65)
    dict[uni] = int(input())



s = []
size=0
for char in m:
    if char == '*':
        s.append(s.pop() * s.pop())
    elif char == '/':
        a = s.pop()
        b = s.pop()
        s.append(b/a)
    elif char == '+':
        s.append(s.pop() + s.pop())
    elif char == '-':
        a = s.pop()
        b = s.pop()
        s.append(b-a)
    else:
        s.append(dict[char])
        size+=1

print("{:.2f}".format(s[0]))
