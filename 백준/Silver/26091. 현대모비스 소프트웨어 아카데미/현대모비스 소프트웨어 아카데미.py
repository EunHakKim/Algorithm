import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ability = list(map(int, input().split()))

ability.sort()
left, right = 0, n - 1
ans = 0

while left < right:
    if ability[left] + ability[right] >= m:
        left += 1
        right -= 1
        ans += 1
        continue

    left += 1

print(ans)
