n=input()
nums=[]

for i in range(len(n)):
    nums.append(int(n[i]))

nums.sort()

for i in range(len(n)-1,-1,-1):
    print(nums[i],end="")