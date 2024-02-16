N=int(input())

def check(arr):
    aws = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            aws = max(aws, cnt)

        cnt = 1
        for j in range(1, N):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            aws = max(aws, cnt)
    
    return aws

candy=[list(input()) for _ in range(N)]
result=1

for i in range(N):
    for j in range(N):
        if j!=N-1:
            if candy[i][j]!=candy[i][j+1]:
                candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j]
                temp=check(candy)
                result=max(result,temp)
                candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j]

for i in range(N):
    for j in range(N):
        if i!=N-1:
            if candy[i][j]!=candy[i+1][j]:
                candy[i][j],candy[i+1][j]=candy[i+1][j],candy[i][j]
                temp=check(candy)
                result=max(result,temp)
                candy[i][j],candy[i+1][j]=candy[i+1][j],candy[i][j]

print(result)