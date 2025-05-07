import sys
input = sys.stdin.readline
from itertools import combinations

n, c = map(int, input().split())
lst = list(map(int, input().split()))
a, b = lst[: n // 2], lst[n // 2 :]
sum_a, sum_b = [],[]
cnt = 1
for i in range(1, len(a) + 1):
    for j in combinations(a, i):
        temp = sum(j)
        if temp <= c:
            sum_a.append(temp)

for i in range(1, len(b) + 1):
    for j in combinations(b, i):
        temp = sum(j)
        if temp <= c:
            sum_b.append(temp)
sum_b.sort()

for i in sum_a:
    st, en = 0 , len(sum_b)
    while st < en:
        mid = (st + en) // 2
        if i + sum_b[mid] <= c:
            st = mid + 1
        else:
            en = mid
    cnt += en
print(len(sum_a) + len (sum_b) + cnt)