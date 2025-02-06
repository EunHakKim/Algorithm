import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
tables = [tuple(map(int, input().split())) for _ in range(m)]

for y in range(n):
    for x in range(1, n):
        nums[x][y] += nums[x - 1][y]

for x in range(n):
    for y in range(1, n):
        nums[x][y] += nums[x][y - 1]

for x1, y1, x2, y2 in tables:
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    ans = nums[x2][y2]
    if x1 != 0:
        ans -= nums[x1 - 1][y2]
    if y1 != 0:
        ans -= nums[x2][y1 - 1]
    if x1 != 0 and y1 != 0:
        ans += nums[x1 - 1][y1 - 1]
    print(ans)
