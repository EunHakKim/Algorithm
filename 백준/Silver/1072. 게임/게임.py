import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x
st, en = 1, x

if z >= 99:
    print(-1)
    exit()

while st < en:
    mid = (st + en) // 2
    rate = (y + mid) * 100 // (x + mid)

    if rate > z:
        en = mid
    else:
        st = mid + 1

print(st)
