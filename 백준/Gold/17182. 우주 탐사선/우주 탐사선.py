import sys
input = sys.stdin.readline

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
visited[k] = True
result = 10**9

for s in range(n):
    for a in range(n):
        for b in range(n):
            t[a][b] = min(t[a][b], t[a][s] + t[s][b])

def dfs(idx, time):
    global result
    if False not in visited:
        result = min(result, time)
        return

    for i in range(len(t[idx])):
        if not visited[i]:
            visited[i] = True
            dfs(i, time + t[idx][i])
            visited[i] = False
    
dfs(k, 0)
print(result)