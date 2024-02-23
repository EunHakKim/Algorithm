N=int(input())
A=list(map(int,input().split()))
dp=[1]*N

for i in range(1,N):
    for j in range(i):
        if A[i]>A[j]:
            dp[i] = max(dp[i], dp[j]+1)

x = max(dp)
print(x)

result=[]
for i in range(N-1,-1,-1):
    if dp[i]==x:
        result.append(A[i])
        x-=1
result.reverse()
for y in result:
    print(y, end=" ")