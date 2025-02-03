import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans, i = 0, 0

for x in nums:
    if x == 1:
        i += 1
    else:
        ans += (i * (i + 1) // 2)
        i = 0
print(ans + (i * (i + 1) // 2))