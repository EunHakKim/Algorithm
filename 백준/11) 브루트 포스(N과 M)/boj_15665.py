N, M = map(int,input().split())
nums=list(map(int,input().split()))
nums=list(set(nums))
nums=sorted(nums)
result=[]

def backtracking():
    if len(result)==M:
        print(" ".join(map(str,result)))
        return
    
    for x in nums:
        result.append(x)
        backtracking()
        result.pop()

backtracking()