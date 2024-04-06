import sys
input = sys.stdin.readline
ans = []

def solve(N, graph, order):
    rank = [-1 for i in range(N+1)]

    for i in range(1,N+1) :
        rank[order[i-1]] = i 
    
    
    for i in range(1,N+1) :
        graph[i] = sorted(graph[i], key=lambda x : rank[x])

    visited[1]=True
    ans.append(1)
    dfs(1,N)

def dfs(idx, N):
    if len(ans)==N:
        if ans == order :
            print(1)
        else :
            print(0)
        exit()

    for i in graph[idx]:
        if not visited[i]:
            visited[i]=True
            ans.append(i)
            dfs(i,N)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(1,N) :
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

order = list(map(int,input().split()))

solve(N,graph,order)