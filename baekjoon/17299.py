n = int(input())
inputs = list(map(int,input().split()))
stack = []
counts = {}
ans = [-1]*n
size = 0

for i in inputs:
    if not i in counts:
        counts[i] = 1
    else:
        counts[i]+=1


for i in range(n):
    while size:
        sv = stack[size-1]
        if counts[inputs[i]] > counts[inputs[sv]]:
            ans[sv] = inputs[i]
            stack.pop()
            size-=1
        else:
            break

    stack.append(i)
    size+=1

print(' '.join(list(map(str,ans))))
