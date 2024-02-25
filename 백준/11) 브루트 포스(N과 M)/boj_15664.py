N, M = map(int,input().split())
nums=list(map(int,input().split()))
nums=sorted(nums)
fnum=list(set(nums))
fnum=sorted(fnum)
result=[]

def backtracking():
    if len(result)==M:
        print(" ".join(map(str,result)))
        return
    
    for x in fnum:
        if len(result)==0:
            result.append(x)
            backtracking()
            result.pop()
        elif result.count(x)<nums.count(x) and result[-1]<=x:
            result.append(x)
            backtracking()
            result.pop()

backtracking()