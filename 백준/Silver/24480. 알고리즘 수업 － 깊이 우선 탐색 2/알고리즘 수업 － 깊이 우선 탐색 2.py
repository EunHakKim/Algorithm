import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
depth = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for arr in graph:
    arr.sort(reverse=True)

def dfs(x):
    global depth
    depth += 1
    visited[x] = depth
    for nx in graph[x]:
        if visited[nx] == 0:
            dfs(nx)

dfs(r)
for i in range(1, n + 1):
    print(visited[i])