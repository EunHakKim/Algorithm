N, M = map(int,input().split())
result=[]

def backtracking():
    if len(result)==M:
        print(" ".join(map(str,result)))
        return
    
    for i in range(1,N+1):
        if len(result)==0:
            result.append(i)
            backtracking()
            result.pop()
        elif result[-1]<=i:
            result.append(i)
            backtracking()
            result.pop()

backtracking()