import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
bus = [list(map(int, input().split())) for _ in range(m)]
dist = [INF] * (n + 1)

def bellman_ford(st):
    dist[st] = 0
    for i in range(n):
        for j in range(m):
            current, next, edge_cost = bus[j]
            if dist[current] != INF and dist[next] > dist[current] + edge_cost:
                dist[next] = dist[current] + edge_cost
                if i == n - 1:
                    print(-1)
                    exit()
                
bellman_ford(1)

for i in range(2, n + 1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])