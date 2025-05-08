import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [list(map(int, list(input().strip()))) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if nums[i][j] == 1:
            nums[i][j] = min(nums[i - 1][j], nums[i][j - 1], nums[i - 1][j - 1]) + 1

ans = 0
for x in nums:
    temp = max(x)
    ans = max(ans, temp)
print(ans ** 2)