import sys
input = sys.stdin.readline

k, n = map(int,input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))

def check(temp):
    add = 0
    for lan in lans:
        add += lan // temp
    return add

def search(st, en, target):
    if st == en:
        if check(st) >= n:
            print(st)
        else:
            print(st - 1)
        return

    mid = (st + en) // 2
    if check(mid) < target:
        search(st, mid, target)
    else:
        search(mid + 1, en, target)

search(1, max(lans), n)
    