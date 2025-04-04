import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
visited[r], cnt = 1, 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(v):
    global cnt
    for nv in graph[v]:
        if visited[nv] == 0:
            cnt += 1
            visited[nv] = cnt
            dfs(nv)

dfs(r)
for i in range(1, n + 1):
    print(visited[i])