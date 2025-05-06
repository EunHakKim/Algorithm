import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
a.sort()
left, right, ans = 0, n - 1, 0

while left < right:
    sumv = a[left] + a[right]
    if sumv > x:
        right -= 1
    elif sumv < x:
        left += 1
    else:
        ans += 1
        left += 1
        right -= 1

print(ans)