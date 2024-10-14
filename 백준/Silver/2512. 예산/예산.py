import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
target_list = list(map(int, input().split()))
m = int(input())

target_list.sort()

def check(mid):
    global n
    temp = 0
    for i in range(n):
        if target_list[i] < mid:
            temp += target_list[i]
        else:
            temp += (n - i) * mid
            break
    return temp

def search(st, en, target):
    if st == en:
        result = check(st)
        if result <= target:
            print(st)
        else:
            print(st - 1)
        return

    mid = (st + en) // 2
    result = check(mid)

    if result >= target:
        search(st, mid, target)
    else:
        search(mid + 1, en, target)

search(0, target_list[-1], m)