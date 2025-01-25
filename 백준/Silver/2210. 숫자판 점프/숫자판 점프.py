import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

nums = [list(map(int, input().split())) for _ in range(5)]
ans = set([])

def dfs(x, y, num, depth):
    if depth >= 6:
        ans.add(num)
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, int(str(num) + str(nums[ny][nx])), depth + 1) 

for x in range(5):
    for y in range(5):
        dfs(x, y, nums[y][x], 1)

print(len(ans))