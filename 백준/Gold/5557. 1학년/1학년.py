import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
result = nums.pop()

dp = [[0] * 21 for _ in range(n - 1)]
dp[0][nums[0]] = 1

for i in range(1, n - 1):
    for j in range(21 - nums[i]):
        dp[i][j + nums[i]] += dp[i - 1][j]

    for j in range(nums[i], 21):
        dp[i][j - nums[i]] += dp[i - 1][j]

#print(*dp, sep="\n")
print(dp[n - 2][result])