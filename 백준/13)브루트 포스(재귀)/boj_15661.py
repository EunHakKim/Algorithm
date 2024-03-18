import sys

def backtracking(depth, index):
    global result
    if depth>N//2:
        return
    elif depth>=1:
        start,link=0,0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start+=S[i][j]
                elif not visited[i] and not visited[j]:
                    link+=S[i][j]
        result=min(result, abs(start-link))  
        if result==0:
            print(0)
            exit()  

    for i in range(index, N):
        if not visited[i]:
            visited[i]=True
            backtracking(depth+1, i+1)
            visited[i]=False

N=int(input())
S=[list(map(int,input().split())) for _ in range(N)]
visited=[False for _ in range(N)]
result=sys.maxsize

backtracking(0,0)
print(result)