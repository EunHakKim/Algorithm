import sys
input = sys.stdin.readline

m, n = map(int, input().split())
l = list(map(int, input().split()))
st, en = 0, max(l)

def check(mid):
    if mid == 0:
        return True
    cnt = 0
    for snack in l:
        cnt += snack // mid
    return cnt >= m

while st < en:
    mid = (st + en) // 2
    if check(mid):
        st = mid + 1
    else:
        en = mid

if check(st):
    print(st)
else:
    print(st - 1)