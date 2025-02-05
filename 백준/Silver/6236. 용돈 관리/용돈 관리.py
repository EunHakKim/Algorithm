import sys
input = sys.stdin.readline

n, m = map(int, input().split())
spent = []
for _ in range(n):
    spent.append(int(input()))
ans = 1000000000

def check(money):
    i = 1
    current_money = money
    for x in spent:
        if current_money < x:
            i += 1
            current_money = money - x
        else:
            current_money -= x
    return i

def binary_search(st, en):
    global ans
    while st < en:
        mid = (st + en) // 2

        if check(mid) > m:
            st = mid + 1
        else:
            ans = min(mid, ans)
            en = mid

binary_search(max(spent), 1000000000)
print(ans)

