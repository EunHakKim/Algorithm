T=int(input())

for _ in range(T):
    n=int(input())
    sum=[0,1,2,4]
    for i in range(4,n+1):
        sum.append(sum[i-1]+sum[i-2]+sum[i-3])
    print(sum[n])

