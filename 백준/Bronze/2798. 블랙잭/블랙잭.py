n,m=map(int,input().split())
nums=list(map(int,input().split()))
sum=[]

for x in nums:
    for y in nums:
        for z in nums:
            if x!=y and x!=z and y!=z:
                sum.append(x+y+z)

max=0

for x in sum:
    if x<=m and x>max:
        max=x

print(max)