import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    arr = list(map(str,input().strip()))
    for x in arr:
        graph[i].append(int(x))
table = [[sys.maxsize] * n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dijkstra(stx, sty):
    q = []
    heapq.heappush(q, (0, stx, sty))
    table[sty][stx] = 0
    while q:
        w, x, y = heapq.heappop(q)
        if table[y][x] < w:
            continue
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == 1:
                    if table[y][x] < table[ny][nx]:
                        table[ny][nx] = table[y][x]
                        heapq.heappush(q, (table[y][x], nx, ny))
                else:
                    if table[y][x] + 1 < table[ny][nx]:
                        table[ny][nx] = table[y][x] + 1
                        heapq.heappush(q, (table[y][x] + 1, nx, ny))

dijkstra(0, 0)

print(table[n-1][n-1])