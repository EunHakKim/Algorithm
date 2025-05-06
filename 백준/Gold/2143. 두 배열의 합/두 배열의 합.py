import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
asum, bsum = [], []

for i in range(1, n + 1):
    vsum = sum(a[:i])
    asum.append(vsum)
    for j in range(i, n):
        vsum += a[j]
        vsum -= a[j - i]
        asum.append(vsum)

for i in range(1, m + 1):
    vsum = sum(b[:i])
    bsum.append(vsum)
    for j in range(i, m):
        vsum += b[j]
        vsum -= b[j - i]
        bsum.append(vsum)

asum.sort() # 오름차순
bsum.sort(reverse=True) # 내림차순
ap, bp, ans = 0, 0, 0
while ap < len(asum) and bp < len(bsum):
    vsum = asum[ap] + bsum[bp]
    if vsum < t:
        ap += 1
    elif vsum > t:
        bp += 1
    else:
        acnt, bcnt = 0, 0
        while asum[ap] == asum[ap + acnt]:
            acnt += 1
            if ap + acnt >= len(asum):
                break
        while bsum[bp] == bsum[bp + bcnt]:
            bcnt += 1
            if bp + bcnt >= len(bsum):
                break
        ans += acnt * bcnt
        ap += acnt
        bp += bcnt

print(ans)