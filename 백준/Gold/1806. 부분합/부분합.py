import sys
input = sys.stdin.readline

n, s = map(int,input().split())
arr = list(map(int, input().split()))
sums = 0
ans = sys.maxsize
left = 0

for right in range(n):
    sums += arr[right]
    while sums >= s:
        ans = min(ans, right - left + 1)
        sums -= arr[left]
        left += 1

if ans == sys.maxsize:
    print(0)
else:
    print(ans)
