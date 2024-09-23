import sys
input = sys.stdin.readline

n = int(input())
nodes = list(map(int,input().split()))
target = int(input())
start = 0
graph = [[] for _ in range(n)]
ans=0

for i in range(n):
    if nodes[i]==-1:
        start = i
    else:
        graph[nodes[i]].append(i)

if start==target:
    print(0)
    exit()

def dfs(t):
    global ans
    if len(graph[t])==0 or (len(graph[t])==1 and target in graph[t]):
        ans+=1
    for i in graph[t]:
        if i!=target:
            dfs(i)
dfs(start)
print(ans)
