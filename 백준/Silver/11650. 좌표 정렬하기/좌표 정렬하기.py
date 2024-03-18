import sys

n=int(input())

p=[]

for i in range(n):
    xy=list(map(int,sys.stdin.readline().split()))
    p.append(xy)

p.sort()

for i in range(n):
    print(p[i][0],p[i][1])