import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
cows = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cows[a - 1].append((b - 1, c))
    cows[b - 1].append((a - 1, c))
dist = [10**9] * n

def dijkstra(st):
    q = []
    heapq.heappush(q, (0, st))
    dist[st] = 0

    while q:
        d, cur = heapq.heappop(q)

        if dist[cur] < d:
            continue

        for i, j in cows[cur]:
            if d + j < dist[i]:
                dist[i] = d + j
                heapq.heappush(q, (d + j, i))

dijkstra(0)
print(dist[n - 1])