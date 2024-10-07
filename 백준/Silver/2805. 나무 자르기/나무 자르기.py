import sys
input = sys.stdin.readline

n, m = map(int,input().split())
trees = list(map(int, input().split()))
ans = 0

def cal_height(target):
    ans = 0
    for tree in trees:
        if tree > target:
            ans += tree - target
    return ans

def search(st, en, target):
    if st == en:
        if cal_height(st) >= target:
            print(st)
        else:
            print(st - 1)
        return
    
    mid = (st + en) // 2
    if cal_height(mid) <= target:
        search(st, mid, target)
    else:
        search(mid + 1, en, target)

search(0, max(trees), m)