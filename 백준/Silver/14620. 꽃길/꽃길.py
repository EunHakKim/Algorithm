import sys
input = sys.stdin.readline

n = int(input())
prices = [list(map(int, input().split())) for _ in range(n)]
flowers = set([])
ans = sys.maxsize
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check():
    global ans
    chk = set([])
    p = 0
    for x, y in flowers:
        chk.add((x, y))
        p += prices[x][y]
        for k in range(4):
            chk.add((x + dx[k], y + dy[k]))
            p += prices[x + dx[k]][y + dy[k]]
    if len(chk) == 15:
        ans = min(ans, p)
    return

def back():
    if len(flowers) == 3:
        check()
        return

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if (i, j) not in flowers:
                flowers.add((i, j))
                back()
                flowers.remove((i, j))

back()
print(ans)