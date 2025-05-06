import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

each = sum(nums[:k])
ans = each
for i in range(k, n):
    each += nums[i]
    each -= nums[i - k]

    ans = max(ans, each)

print(ans)