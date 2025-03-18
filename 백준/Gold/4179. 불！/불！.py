import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())
miro = [list(input().strip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
jihun = ()
fire = deque([])
for i in range(r):
    for j in range(c):
        if miro[i][j] == 'J':
            jihun = (j, i)
            miro[i][j] = '.'
        if miro[i][j] == 'F':
            fire.append((j, i))

def bfs(x, y):
    global fire
    queue = deque([(x, y)])
    visited[y][x] = 1
    chk = 0
    while queue:
        cx, cy = queue.popleft()
        #탈출 체크
        if cx == 0 or cx == c - 1 or cy == 0 or cy == r - 1:
            print(visited[cy][cx])
            exit()

        #불 확산
        if chk < visited[cy][cx]:
            chk += 1
            for _ in range(len(fire)):
                fx, fy = fire.popleft()
                for k in range(4):
                    nx, ny = fx + dx[k], fy + dy[k]
                    if 0 <= nx < c and 0 <= ny < r:
                        if miro[ny][nx] == '.':
                            miro[ny][nx] = 'F'
                            fire.append((nx, ny))
        
        #지훈 이동
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < c and 0 <= ny < r:
                if visited[ny][nx] == 0 and miro[ny][nx] == '.':
                    visited[ny][nx] = visited[cy][cx] + 1
                    queue.append((nx, ny))
        
        
bfs(jihun[0], jihun[1])
print("IMPOSSIBLE")