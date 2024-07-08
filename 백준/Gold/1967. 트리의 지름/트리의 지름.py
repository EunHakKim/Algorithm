import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n=int(input())
graph = [[] for _ in range(n+1)]
weight = [-1]*(n+1)
for _ in range(n-1):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(index):
    for x, y in graph[index]:
        if weight[x]==-1:
            weight[x]=weight[index]+y
            dfs(x)

weight[1]=0
dfs(1)
edge=weight.index(max(weight))
weight=[-1]*(n+1)
weight[edge]=0
dfs(edge)
print(max(weight))