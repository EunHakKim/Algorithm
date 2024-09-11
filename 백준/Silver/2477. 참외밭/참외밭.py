import sys
input = sys.stdin.readline

k = int(input())
graph = [list(map(int,input().split())) for _ in range(6)]
a = []
b = []
ans = []

for i in range(6):
    if graph[i][0] in b:
        b.remove(graph[i][0])
        a.append(graph[i][0])
    else:
        b.append(graph[i][0])

for i in range(6):
    if graph[i][0] in b:
        ans.append(graph[i][1])
        if len(ans)==2:
            temp = i
            while True:
                temp = (temp + 1) % 6
                if graph[temp][0] in a:
                    ans.append(graph[(temp + 1) % 6][1])
                    ans.append(graph[(temp + 2) % 6][1])
                    print(k*(ans[0]*ans[1]-ans[2]*ans[3]))
                    exit()
    