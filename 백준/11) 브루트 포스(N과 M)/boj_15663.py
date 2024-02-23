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
        if result.count(x)<nums.count(x):
            result.append(x)
            backtracking()
            result.pop()

backtracking()