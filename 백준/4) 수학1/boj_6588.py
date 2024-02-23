import sys

prime=[True]*1000001
for i in range(2,1001):
    if prime[i]:
        for j in range(i*2,1000001,i):
            prime[j]=False

prime[1]=False


while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    temp=0
    for i in range(3,n//2+1,2):
        if prime[i] and prime[n-i]:
            temp=1
            print(f"{n} = {i} + {n-i}")
            break
    if temp==0:
        print("Goldbach's conjecture is wrong.")