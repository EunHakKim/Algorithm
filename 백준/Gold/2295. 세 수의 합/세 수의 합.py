import sys
input = sys.stdin.readline
n = int(input())
u = [int(input()) for _ in range(n)]
u.sort()

u_sum = set()
for x in u:
    for y in u:
        u_sum.add(x+y)

for i in range(n-1, -1, -1):
    for j in range(i+1):
        if u[i]-u[j] in u_sum:
            print(u[i])
            exit()