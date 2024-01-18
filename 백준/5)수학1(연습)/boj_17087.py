import math

N,S=map(int,input().split())

A=list(map(int,input().split()))
B=[]

for x in A:
    B.append(abs(x-S))

result=B[0]

for i in range(1,len(B)):
    result=math.gcd(result,B[i])

print(result)