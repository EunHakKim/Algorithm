N=int(input())
T=[]
P=[]
for _ in range(N):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)
days=[]
profits=[]
result=[]

def backtracking():
    if len(days)!=0 and days[-1]+T[days[-1]]==N:
        result.append(sum(profits))
        return
    elif len(days)!=0 and days[-1]+T[days[-1]]>N:
        result.append(sum(profits)-profits[-1])
        return

    for i in range(N):
        if len(days)==0 or (days[-1]+T[days[-1]]<=i):
            days.append(i)
            profits.append(P[i])
            backtracking()
            days.pop()
            profits.pop()

backtracking()
print(max(result))