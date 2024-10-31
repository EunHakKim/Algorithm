import sys
input = sys.stdin.readline

def bellman_ford():
    for i in range(n):
        for j in range(len(road)):
            s, e, t = road[j]
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n - 1:
                    return True
    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    road = []
    dist = [1e9] * (n + 1)

    for _ in range(m):
        s, e, t = map(int, input().split())
        road.append((s, e, t))
        road.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        road.append((s, e, (-1) * t))

    if bellman_ford():
        print("YES")
    else:
        print("NO")