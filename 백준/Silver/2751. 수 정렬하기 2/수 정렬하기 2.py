import sys

n=int(input())
nums=[]

for i in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for i in range(n):
    print(nums[i])