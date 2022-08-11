n, k = list(map(int,input().split()))

q = []
ans = []
begin, end = 1, 1
count = 1

q.append(0)
for i in range(n):
    q.append(i+1)
    end+=1

while end-begin:
    if count%k == 0:
        ans.append(q[begin])
        begin+=1
    else:
        q.append(q[begin])
        begin+=1
        end+=1
    count+=1

print("<" + str(ans)[1:-1] + ">")

