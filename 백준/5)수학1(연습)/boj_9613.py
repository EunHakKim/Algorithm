import math

t=int(input())

for i in range(t):
    nums=list(map(int,input().split()))
    nums.remove(nums[0])
    result=0

    for j in range(len(nums)-1):
        for k in range(j+1,len(nums)):
            result+=math.gcd(nums[j],nums[k])
    print(result)