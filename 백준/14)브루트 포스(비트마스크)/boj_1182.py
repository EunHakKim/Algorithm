import itertools

N, S= map(int,input().split())
arr=list(map(int,input().split()))
cnt=0 

for i in range(1,N+1):
    per=itertools.combinations(arr,i)
    for x in per:
        if sum(x)==S:
            cnt+=1

print(cnt)