strs = input().strip()
n = int(input())


left, right = [], []
for char in strs:
    left.append(char)

for i in range(n):
    m = input().strip()
    if m == 'L':
        if left:
            right.append(left[-1])
            left.pop()
    elif m == 'D':
        if right:
            left.append(right[-1])
            right.pop()
    elif m == 'B':
        if left:
            left.pop()
    else:
        p, value = m.split()
        left.append(value)

while left:
    right.append(left[-1])
    left.pop()
while right:
    print(right[-1],end='')
    right.pop()

