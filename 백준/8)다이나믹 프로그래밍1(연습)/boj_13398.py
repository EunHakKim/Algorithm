n=int(input())

a=list(map(int,input().split()))
dpl=[x for x in a]
dpr=[x for x in a]
dp=[x for x in a]

for i in range(n):
    if i>0:
        dpl[i]=max(dpl[i],dpl[i]+dpl[i-1])

for i in range(n-1,-1,-1):
    if i<n-1:
        dpr[i]=max(dpr[i],dpr[i]+dpr[i+1])

for i in range(n):
    if 0<i<n-1:
        dp[i]=dpl[i-1]+dpr[i+1]

print(max(max(dpl),max(dp)))