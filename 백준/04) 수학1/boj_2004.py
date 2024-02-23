n,m=map(int,input().split())
k=n-m
N,M,K=n,m,k
five=[0]*3
two=[0]*3

while n//5>0:
    five[0]+=n//5
    n//=5

while k//5>0:
    five[1]+=k//5
    k//=5

while m//5>0:
    five[2]+=m//5
    m//=5

while N//2>0:
    two[0]+=N//2
    N//=2

while K//2>0:
    two[1]+=K//2
    K//=2

while M//2>0:
    two[2]+=M//2
    M//=2

if five[0]-five[1]-five[2]<two[0]-two[1]-two[2]:
    print(five[0]-five[1]-five[2])
else:
    print(two[0]-two[1]-two[2])