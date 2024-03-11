import itertools
import sys

N=int(sys.stdin.readline())
W=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
nums=[x for x in range(N)]

per=itertools.permutations(nums)
result=sys.maxsize

for i in per:
    if W[i[-1]][i[0]]==0:
        continue
    else:
        s=W[i[-1]][i[0]]
    for j in range(N-1):
        if W[i[j]][i[j+1]]==0 or s>result:
            s=-1
            break
        else:
            s+=W[i[j]][i[j+1]]
    if s!=-1:
        result=min(result,s)

print(result)