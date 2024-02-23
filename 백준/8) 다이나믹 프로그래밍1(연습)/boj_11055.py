N=int(input())
A=list(map(int,input().split()))
dp=[x for x in A]

for i in range(1,N):
    for j in range(i):
        if A[i]>A[j]:
            dp[i]=max(dp[j]+A[i],dp[i])

print(max(dp))