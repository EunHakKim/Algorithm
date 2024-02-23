N, M = map(int,input().split())
nums=list(map(int,input().split()))
nums=sorted(nums)
result=[]

def backtracking():
    if len(result)==M:
        print(" ".join(map(str,result)))
        return
    
    for x in nums:
        if len(result)==0:
            result.append(x)
            backtracking()
            result.pop()
        elif result[-1]<=x:
            result.append(x)
            backtracking()
            result.pop()

backtracking()