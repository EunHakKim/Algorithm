import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
ans = []

for i in range(1, 11):
    for j in combinations(range(10), i): 
        num = sorted(list(j), reverse=True)
        ans.append(int("".join(map(str, num))))

ans.sort()
if len(ans) > n:
    print(ans[n])
else:
    print(-1)