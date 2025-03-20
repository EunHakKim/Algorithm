import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
people = list(map(int, input().split()))
animals = [tuple(map(int, input().split())) for _ in range(n)]
cnt = 0

people.sort()

def chk(x):
    st, en = 0, m - 1
    while st < en:
        mid = (st + en) // 2
        if people[mid] < x:
            st = mid + 1
        else:
            en = mid
    return st

for x, y in animals:
    person = chk(x)
    if abs(people[person] - x) + y <= l:
        cnt += 1

print(cnt)