import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cnt = 0
ans = 0

def bfs():
    queue=deque()
    queue.append([0,0])
    visited[0][0]=cave[0][0]
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[y][x] + cave[ny][nx] < visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + cave[ny][nx]
                    queue.append([nx, ny])

    return visited[n-1][n-1]

while True:
    n = int(input())
    cnt += 1
    if n == 0:
        exit()

    cave = [list(map(int, input().split())) for _ in range(n)]
    visited = [[10**9] * n for _ in range(n)]
    print("Problem " + str(cnt) + ":", bfs())
