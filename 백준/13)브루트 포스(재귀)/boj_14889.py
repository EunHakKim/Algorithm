import itertools
import math
import sys

N=int(input())
nums=[i for i in range(N)]
S=[list(map(int,input().split())) for _ in range(N)]

com=list(itertools.combinations(nums,N//2))
result=sys.maxsize
size=math.comb(N,N//2)

for i in range(size//2):
    start=0
    for j in range(N//2):
        for k in range(N//2):
            start+=S[com[i][j]][com[i][k]]
    link=0
    for j in range(N//2):
        for k in range(N//2):
            link+=S[com[size-1-i][j]][com[size-1-i][k]]

    result=min(result,abs(start-link))
    if result==0:
        break

print(result)