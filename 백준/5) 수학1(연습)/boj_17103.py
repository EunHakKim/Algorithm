import sys

T=int(sys.stdin.readline())

prime=[True]*1000001

for i in range(2,1001):
    if prime[i]:
        for j in range(i+i,1000001,i):
            prime[j]=False

prime[0],prime[1]=False,False

for i in range(T):
    result=0
    N=int(sys.stdin.readline())
    for j in range(N//2+1):
        if prime[j] and prime[N-j]:
            result+=1
    print(result)