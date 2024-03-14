n=int(input())

i=0
sum=0

while sum<n:
    i+=1
    sum+=i

if i%2==0:
    print(f"{n-sum+i}/{1-n+sum}")
else:
    print(f"{1-n+sum}/{n-sum+i}")