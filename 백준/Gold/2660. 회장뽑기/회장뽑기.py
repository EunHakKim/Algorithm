import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
score = [[10**9] * (n) for _ in range(n)]
for i in range(n):
    score[i][i]=0

master = []
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    score[a - 1][b - 1] = 1
    score[b - 1][a - 1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            score[a][b] = min(score[a][b], score[a][k] + score[k][b])

for x in score:
    master.append(max(x))

ans = min(master)
print(ans, master.count(ans))

for i in range(n):
    if master[i]==ans:
        print(i + 1, end = " ")
