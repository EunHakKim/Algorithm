import sys

n=int(input())
nums=[0]*10001

for i in range(n):
    num=int(sys.stdin.readline())
    nums[num]+=1

for i in range(10001):
    if nums[i]!=0:
        for j in range(nums[i]):
            print(i)