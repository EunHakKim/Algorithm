import sys
input = sys.stdin.readline
n, l = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    j=0
    same=1
    while True:
        if j==n-1:
            ans+=1
            break
        if graph[i][j]==graph[i][j+1]:
            j+=1
            same+=1
            continue
        elif graph[i][j]+1==graph[i][j+1] and same>=l:
            same = 1
            j+=1
            continue
        elif j<=n-1-l and graph[i][j]==graph[i][j+1]+1:
            temp = True
            for k in range(l-1):
                if graph[i][j+1]!=graph[i][j+2+k]:
                    temp = False
            if temp:
                same = 0
                j+=l
                continue
            else:
                break
        else:
            break

for i in range(n):
    j=0
    same=1
    while True:
        if j==n-1:
            ans+=1
            break
        if graph[j][i]==graph[j+1][i]:
            j+=1
            same+=1
            continue
        elif graph[j][i]+1==graph[j+1][i] and same>=l:
            same = 1
            j+=1
            continue
        elif j<=n-1-l and graph[j][i]==graph[j+1][i]+1:
            temp = True
            for k in range(l-1):
                if graph[j+1][i]!=graph[j+2+k][i]:
                    temp = False
            if temp:
                same = 0
                j+=l
                continue
            else:
                break
        else:
            break

print(ans)