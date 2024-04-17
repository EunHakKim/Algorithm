from collections import deque

N, K=map(int,input().split())
depth=[-1]*200001

queue=deque([N])
depth[N]=0
while queue:
    temp=queue.popleft()
    i=temp*2
    while 0<=i<=2*K:
        if depth[i]==-1:
            depth[i]=depth[temp]
            queue.append(i)
        else:
            break
        i=i*2
    for j in [temp-1,temp+1]:
        if 0<=j<=100000:
            if depth[j]==-1:
                depth[j]=depth[temp]+1
                queue.append(j)
    if depth[K]!=-1:
        print(depth[K])
        exit()