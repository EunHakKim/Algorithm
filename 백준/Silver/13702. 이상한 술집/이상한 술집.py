n, k = map(int, input().split())
ju = [int(input()) for _ in range(n)]
st, en, ans = 1, max(ju), 0

def check(mac):
    cnt = 0
    for j in ju:
        cnt += j // mac
    if cnt >= k:
        return True
    return False

while st < en:
    mid = (st + en) // 2

    if check(mid):
        ans = max(ans, mid)
        st = mid + 1
    else:
        en = mid - 1
if check(st):
    ans = max(ans, st)
print(ans)