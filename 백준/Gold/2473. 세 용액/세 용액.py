import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
min_value = sys.maxsize
ans = []

for i in range(1, n - 1):
    left, right = 0, n - 1
    while left < i and right > i:
        temp = nums[left] + nums[i] + nums[right]

        if abs(temp) < min_value:
            ans = [nums[left], nums[i], nums[right]]
            min_value = abs(temp)

        if temp > 0:
            right -= 1
        else:
            left += 1

print(*ans)