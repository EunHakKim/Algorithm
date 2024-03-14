n,m=map(int,input().split())
num=[]
sum=[]
for i in range(2*n):
    a=list(map(int,input().split()))
    num.append(a)

for i in range(n):
    b=[]
    for j in range(m):
        b.append(num[i][j]+num[i+n][j])
    sum.append(b)    

for i in range(n):
    for j in range(m):
        print(sum[i][j], end=" ")
    print()    