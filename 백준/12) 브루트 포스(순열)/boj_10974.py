N=int(input())
result=[]

def backtracking():
    if len(result)==N:
        print(" ".join(map(str,result)))
        return
    
    for i in range(1,N+1):
        if i not in result:
            result.append(i)
            backtracking()
            result.pop()

backtracking()