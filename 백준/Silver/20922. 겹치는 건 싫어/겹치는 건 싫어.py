import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

st, en = 0, 0
chk = [0] * 100001
ans, cnt = 0, 0

while en < n:
    if chk[a[en]] < k:
        chk[a[en]] += 1
        cnt += 1
        en += 1
    else:
        ans = max(ans, cnt)
        cnt -= 1
        chk[a[st]] -= 1
        st += 1
ans = max(ans, cnt)
print(ans)