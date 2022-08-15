n = int(input())
ans = 1
for i in range(1,n+1):
    ans*=i
ans = str(ans)
print(len(ans) - len(ans.rstrip('0')))
