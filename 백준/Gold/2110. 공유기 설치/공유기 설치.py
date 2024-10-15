import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, c = map(int, input().split())
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()

def check(mid):
    global n
    current = home[0]
    cnt = 1
    for i in range(1, n):
        if home[i] >= current + mid:
            cnt += 1
            current = home[i]
    return cnt

def search(st, en, target):
    if st >= en:
        cnt = check(st)
        if cnt >= target:
            print(st)
        else:
            print(st - 1)
        return
        
    mid = (st + en) // 2
    cnt = check(mid)
    if cnt >= target:
        search(mid + 1, en, target)
    else:
        search(st, mid, target)

search(1, home[-1]-home[0], c)