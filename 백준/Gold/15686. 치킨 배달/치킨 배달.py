import sys
input = sys.stdin.readline

n, m = map(int,input().split())
house = []
chicken = []
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        if temp[j] == 1:
            house.append((i,j))
        elif temp[j]==2:
            chicken.append((i,j))

visited = [False]*len(chicken)
minimun = 10**9 

def back(index,cnt):
    global minimun
    if cnt==m:
        clen = 0
        for i in house:
            cmin = 10**9 
            for j in range(len(visited)):
                if visited[j]:
                    distance = abs(i[0]-chicken[j][0])+abs(i[1]-chicken[j][1])
                    cmin = min(cmin, distance)
            clen += cmin
        minimun = min(minimun, clen)
        return

    for i in range(index, len(chicken)):
        if not visited[i]:
            visited[i] = True
            back(i+1,cnt+1)
            visited[i]=False

back(0,0)
print(minimun)