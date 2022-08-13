strs = list(input())
stack = []

while strs:
    stack.append(''.join(strs))
    strs.pop(0)

for char in sorted(stack):
    print(char)
