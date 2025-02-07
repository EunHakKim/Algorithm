import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    ap, bp, ans = 0, 0, 0
    alen, blen = len(a), len(b)
    
    while ap<alen and bp<blen:
        if a[ap] > b[bp]:
            ans += (alen - ap)
            bp += 1
        else:
            ap += 1
    print(ans)
