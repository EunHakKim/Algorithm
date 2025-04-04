import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]
visited = [False] * n
ans = set([])

def back(comb):
    if len(comb) == k:
        temp = ''
        for x in comb:
            temp += str(x)
        ans.add(int(temp))

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            comb.append(cards[i])
            back(comb)
            del comb[-1]
            visited[i] = False
back([])
print(len(ans))