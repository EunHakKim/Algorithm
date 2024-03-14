n=int(input())

p=1000001

for i in range(n):
    sum=i
    num=i
    while num!=0:
        sum+=num%10
        num//=10
    if sum==n and i<p:
        p=i

if p==1000001:
    print(0)
else:
    print(p)