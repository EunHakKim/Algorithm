N=int(input())
P=[10001]+list(map(int,input().split()))
price=[10001]*(N+1)

for i in range(1,N+1):
    if i<len(P):
        price[i]=P[i]
    for j in range(1,i+1):
        price[i]=min(price[i],price[j]+price[i-j])

print(price[N])