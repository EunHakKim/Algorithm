m=int(input())
n=int(input())

nums=[]

for i in range(m,n+1):
    x=0
    for j in range(2,i-1):
        if i%j==0:
            x=1
    if x==0 and i!=1:
        nums.append(i)

if len(nums)!=0:
    print(sum(nums))
    print(nums[0])
else:
    print("-1")