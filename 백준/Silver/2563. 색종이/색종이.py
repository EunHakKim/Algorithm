n=int(input())

sum=0
a=[]

for i in range(10000):
    a.append(0)

for i in range(n):
    x,y=map(int, input().split())
    for j in range(10):
        for k in range(10):
            a[(y+k)*100+x+j]=1

for i in range(10000):
    if a[i]==1:
        sum+=1

print(sum)