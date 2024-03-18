n,m=map(int,input().split())
num=[]

for j in range(n):
    num.append(0)

for i in range(m):
    a=list(map(int,input().split()))
    for z in range(a[0]-1,a[1]):
        num[z]=a[2]

for k in range(n):
    print(num[k],end=" ")