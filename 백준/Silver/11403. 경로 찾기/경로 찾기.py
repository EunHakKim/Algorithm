import sys
input = sys.stdin.readline

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if g[a][k] == 1 and g[k][b] == 1:
                g[a][b] = 1

for arr in g:
    print(*arr)