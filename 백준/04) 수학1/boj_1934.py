import math

n=int(input())

for i in range(n):
    A,B=map(int,input().split())
    print(math.lcm(A,B))