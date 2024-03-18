import sys

n=int(input())

p=[]

for i in range(n):
    [a,b]=list(map(int,sys.stdin.readline().split()))
    p.append([b,a])

p.sort()

for i in range(n):
    print(p[i][1],p[i][0])