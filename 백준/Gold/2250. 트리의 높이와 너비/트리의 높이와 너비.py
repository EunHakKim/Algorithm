import sys
input=sys.stdin.readline

N=int(input().strip())
leftChild = [-1]*(N+1)
rightChild = [-1]*(N+1)
order=[]
depth=[-1]*(N+1)
for _ in range(N):
    a, b, c = map(int,input().strip().split())
    leftChild[a] = b
    rightChild[a] = c

def dfs(index):
    if leftChild[index]!=-1:
        depth[leftChild[index]]=depth[index]+1
        dfs(leftChild[index])
    order.append(index)
    if rightChild[index]!=-1:
        depth[rightChild[index]]=depth[index]+1
        dfs(rightChild[index])

root=-1
for i in range(1,N+1):
    if i not in leftChild and i not in rightChild:
        root=i

depth[root]=1
dfs(root)
level=1
width=1
for i in range(1,max(depth)+1):
    l=N+1
    r=0
    for j in range(N):
        if(depth[order[j]]==i):
            l=min(l,j)
            r=max(r,j)
    if((r-l+1) > width):
        width = r-l+1
        level = i

print(level, width)