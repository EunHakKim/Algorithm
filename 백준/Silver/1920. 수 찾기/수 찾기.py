import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
target_list = list(map(int, input().split()))

a.sort()

def search(st, en, target):
    if st == en:
        if a[st] == target:
            print(1)
        else:
            print(0)
        return
    
    mid = (st + en) // 2
    if a[mid] < target:
        search(mid + 1, en, target)
    else:
        search(st, mid, target)
    
for target in target_list:
    search(0, n-1, target)