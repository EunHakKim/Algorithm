import sys

M, N=map(int,sys.stdin.readline().split())

for i in range(M,N+1):
    if i==1:
        continue
    temp=0
    for j in range(2,int(i**(1/2))+1):
        if i%j==0:
            temp=1
            break
    if temp==0:
        print(i)