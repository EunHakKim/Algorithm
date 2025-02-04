import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, l, r = map(int, input().split())
popul = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
ally = []
people = []
ans = 0

def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    nations = [(x, y)]
    cnt = popul[y][x]
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx]:
                    if l <= abs(popul[cy][cx] - popul[ny][nx]) <= r:
                        cnt += popul[ny][nx]
                        visited[ny][nx] = True
                        nations.append((nx, ny))
                        queue.append((nx, ny))
    if len(nations) > 1:
        ally.append(nations)
        people.append(cnt)

while True:
    visited = [[False] * n for _ in range(n)]
    ally = []
    people = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(j, i)

    if len(ally) == 0:
        print(ans)
        exit()
    ans += 1
    
    for i in range(len(ally)):
        cnt = people[i] // len(ally[i])
        for x, y in ally[i]:
            popul[y][x] = cnt
