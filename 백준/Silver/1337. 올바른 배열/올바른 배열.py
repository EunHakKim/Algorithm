import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())

arr.sort()
st, en, cur, ans = 0, 0, 1, 4

while True:
    en += 1
    cur += 1
    if en >= n:
        break
    if arr[en] - arr[st] <= 4:
        ans = min(ans, 5 - cur)
    else:
        while arr[en] - arr[st] > 4:
            st += 1
            cur -= 1
        ans = min(ans, 5 - cur)
print(ans)