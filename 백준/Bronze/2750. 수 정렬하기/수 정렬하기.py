n=int(input())
nums=[]

for i in range(n):
    m=int(input())
    nums.append(m)

nums.sort()
for i in range(n):
    print(nums[i])
