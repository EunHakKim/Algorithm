import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def check(temp):
    sum = 0
    num = 1
    for x in arr:
        if sum + x > temp:
            num += 1
            sum = x
        else:
            sum += x
    return num

def search(st, en, target):
    if st >= en:
        print(st)
        return

    mid = (st + en) // 2
    num = check(mid)
    if num > target:
        search(mid + 1, en, target)
    else:
        search(st, mid, target)

search(max(arr), 33334 * 10000, m)