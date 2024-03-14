n,m=map(int,input().split())
x=0
y=0

for i in range(1,n+1):
    if n%i==0:
        x+=1
    if x==m:
        y=i
        break

print(y)