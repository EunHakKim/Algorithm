n,m=map(int,input().split())
num=[]

for j in range(n):
    num.append(j+1)

for i in range(m):
    x,y=map(int,input().split())
    z=num[x-1]
    num[x-1]=num[y-1]
    num[y-1]=z

for k in range(n):
    print(num[k],end=" ")