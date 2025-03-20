import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
st, en = 1, k

while st <= en:
    mid = (st + en) // 2

    temp = 0
    for i in range(1, n + 1):
        temp += min(mid//i, n)
    
    if temp >= k:
        en = mid - 1
    else:
        st = mid + 1

print(st)