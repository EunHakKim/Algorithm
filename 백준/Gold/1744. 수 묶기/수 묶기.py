import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
dp = [0] * n
nums.sort()

if n == 1:
    print(nums[0])
    exit()

dp[0] = nums[0]
dp[1] = max(dp[0] + nums[1], nums[0] * nums[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1] + nums[i], dp[i - 2] + nums[i - 1] * nums[i])

print(dp[-1])