import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
hall = [list(input().split()) for _ in range(n)]
teach = []
ans = 'NO'
for y in range(n):
    for x in range(n):
        if hall[y][x] == 'T':
            teach.append((x, y))

def check():
    global ans
    for tx, ty in teach:
        for k in range(4):
            nx, ny = tx, ty
            while 0 <= nx < n and 0 <= ny < n:
                if hall[ny][nx] == 'O':
                    break
                if hall[ny][nx] == 'S':
                    return
                nx += dx[k]
                ny += dy[k]

    ans = 'YES'

def back(depth):
    if depth == 3:
        check()
        return

    for y in range(n):
        for x in range(n):
            if hall[y][x] == 'X':
                hall[y][x] = 'O'
                back(depth + 1)
                hall[y][x] = 'X'

back(0)
print(ans)