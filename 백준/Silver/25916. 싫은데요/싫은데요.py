import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right, ans, cnt = 0, 0, 0, 0

while right < n:
    cnt += a[right]
    if cnt <= m:
        ans = max(ans, cnt)
        right += 1
        continue

    while cnt > m:
        cnt -= a[left]
        left += 1
    ans = max(ans, cnt)
    right += 1

print(ans)