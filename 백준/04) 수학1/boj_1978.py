N=int(input())

nums=list(map(int,input().split()))

result=0

for i in range(N):
    cal=0
    for j in range(1,nums[i]+1):
        if nums[i]%j==0:
            cal+=1
    if cal==2:
        result+=1

print(result)