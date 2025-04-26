import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
target = []
ans = 0
for _ in range(n):
    arr.append(list(input().strip()))
for _ in range(m):
    target.append(list(input().strip()))

arr.sort()

for t in target:
    l = len(t)
    st, en = 0, n - 1
    while st <= en:
        mid = (st + en) // 2
        if t == arr[mid][:l]:
            ans += 1
            break
        elif t > arr[mid][:l]:
            st = mid + 1
        else:
            en = mid - 1

print(ans)