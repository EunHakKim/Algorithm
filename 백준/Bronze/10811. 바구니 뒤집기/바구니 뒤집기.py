n,m=map(int,input().split())
num=[i+1 for i in range(n)]

for j in range(m):
    x,y=map(int,input().split())
    mun=[]
    for k in range(y-x+1):
        mun.append(num[x-1+k])
    for f in range(y-x+1):
        num[x-1+f]=mun[y-x-f]

for z in range(n):
    print(num[z],end=" ")