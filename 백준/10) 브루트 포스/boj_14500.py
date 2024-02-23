N, M = map(int,input().split())

def check (T):
    ans=0
    for i in range(N):
        for j in range(M):
            if j+3<M:
                ans=max(ans, T[i][j]+T[i][j+1]+T[i][j+2]+T[i][j+3])
            if i+1<N and j+1<M:
                ans=max(ans, T[i][j]+T[i][j+1]+T[i+1][j]+T[i+1][j+1])
            if i+2<N and j+1<M:
                ans=max(ans, T[i][j]+T[i+1][j]+T[i+2][j]+T[i+2][j+1])
            if i+2<N and j+1<M:
                ans=max(ans, T[i][j]+T[i+1][j]+T[i+1][j+1]+T[i+2][j+1])
            if i+1<N and j+2<M:
                ans=max(ans, T[i][j]+T[i][j+1]+T[i+1][j+1]+T[i][j+2])
            if i+3<N:
                ans=max(ans, T[i][j]+T[i+1][j]+T[i+2][j]+T[i+3][j])
            if i>0 and j+2<M:
                ans=max(ans, T[i][j]+T[i][j+1]+T[i][j+2]+T[i-1][j+2])
            if i>0 and j+2<M:
                ans=max(ans, T[i][j]+T[i][j+1]+T[i-1][j+1]+T[i-1][j+2])
            if i+2<N and j+1<M:
                ans=max(ans, T[i][j]+T[i+1][j]+T[i+1][j+1]+T[i+2][j])
    return ans

arr=[list(map(int,input().split())) for _ in range(N)]

result=0
result=max(result, check(arr))
arr=arr[::-1]
rseult=max(result, check(arr))
for i in range(N):
    arr[i]=arr[i][::-1]   
result=max(result, check(arr))
arr=arr[::-1]
rseult=max(result, check(arr))

print(result)