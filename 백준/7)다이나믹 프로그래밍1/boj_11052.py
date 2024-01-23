N=int(input())
P=list(map(int,input().split()))
price=[0,P[0]]


for i in range(2,N+1):
    if i<=len(P):
        max=P[i-1]
    else:
        max=0
    for j in range(1,i):
        if (price[j]+price[i-j])>max:
            max=price[j]+price[i-j]
    price.append(max)

print(price[N])