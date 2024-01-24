import sys
T=int(sys.stdin.readline())

sum1=[0,1,0,1,2]
sum2=[0,0,1,1,0]
sum3=[0,0,0,1,1]
for i in range(5,100001):
    sum1.append((sum2[i-1]+sum3[i-1])%1000000009)
    sum2.append((sum1[i-2]+sum3[i-2])%1000000009)
    sum3.append((sum1[i-3]+sum2[i-3])%1000000009)

for _ in range(T):
    n=int(sys.stdin.readline())
    
    print((sum1[n]+sum2[n]+sum3[n])%1000000009)