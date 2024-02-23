n,k=map(int,input().split())
order=0

nums=[i+1 for i in range(n)]
result=[]

for i in range(n):
    order=(order+k-1)%len(nums)
    result.append(str(nums.pop(order)))
                  
print("<",end="")
print(", ".join(result),end="")
print(">")