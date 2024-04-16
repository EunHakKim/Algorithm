from collections import deque

S=int(input())

dist = [[-1]* (S+1) for _ in range(S+1)]
queue = deque()
queue.append((1,0))
dist[1][0] = 0

while queue:
    s,c = queue.popleft()
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] + 1
        queue.append((s,s))
    if s+c <= S and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        queue.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        queue.append((s-1, c))

answer = 1001

for i in range(S+1):
    if dist[S][i] != -1:
        if answer > dist[S][i]:
            answer = dist[S][i]
print(answer)