N, M = map(int,input().split())
result=[]

def backtracking():
    if len(result)==M:
        for x in result:
            print(x, end=" ")
        print()
        return
    for i in range(1,N+1):
        if len(result)==0:
            result.append(i)
            backtracking()
            result.pop()
        elif i > result[-1]:
            result.append(i)
            backtracking()
            result.pop()

backtracking()