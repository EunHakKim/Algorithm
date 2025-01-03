import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
chicken = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for x, y, z in combinations([x for x in range(m)], 3):
    temp = 0
    for i in range(n):
        temp += max(chicken[i][x], chicken[i][y], chicken[i][z])
    ans = max(ans, temp)
print(ans)