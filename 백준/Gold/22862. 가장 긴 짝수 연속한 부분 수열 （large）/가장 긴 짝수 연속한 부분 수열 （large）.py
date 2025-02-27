import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
st, en = 0, 0
rcnt = 0
clen = 1
while st < n and s[st] % 2 == 1:
    st += 1
if st >= n - 1:
    if s[-1] % 2 == 0:
        print(1)
    else:
        print(0)
    exit()

en = st
while en < n - 1 and rcnt < k:
    en += 1
    if s[en] % 2 == 0:
        clen += 1
    else:
        rcnt += 1

ans = clen
if rcnt < k:
    print(ans)
    exit()

while en < n - 1:
    en += 1
    if s[en] % 2 == 0:
        clen += 1
        ans = max(ans, clen)
    else:
        while s[st] % 2 == 0 and st < n:
            clen -= 1
            st += 1
        st += 1

print(ans)