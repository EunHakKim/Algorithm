import sys
input=sys.stdin.readline

N, M = map(int,input().split())
friends=[[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

result=[]

def dfs():
    if len(result)==5:
        print(1)
        exit()
    
    if len(result)==0:
        for i in range(N):        
            result.append(i)
            dfs()
            result.pop()
    else:
        for x in friends[result[-1]]:
            if x not in result:
                result.append(x)
                dfs()
                result.pop()

dfs()
print(0)