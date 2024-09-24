import sys
input = sys.stdin.readline

n, m = map(int,input().split())
big = [[] for _ in range(n+1)]
small = [[] for _ in range(n+1)]
visited = [False]*(n+1)
ans = 0
for _ in range(m):
    a, b = map(int,input().split())
    big[a].append(b)
    small[b].append(a)

def dfs_big(i):
    for x in big[i]:
        if not visited[x]:
            visited[x] = True
            dfs_big(x)

def dfs_small(i):
    for x in small[i]:
        if not visited[x]:
            visited[x] = True
            dfs_small(x)

for i in range(1, n+1):
    visited = [False]*(n+1)
    visited[0] = True
    visited[i] = True
    dfs_big(i)
    dfs_small(i)
    if False not in visited:
        ans += 1 

print(ans)