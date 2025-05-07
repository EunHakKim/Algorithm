import sys
input = sys.stdin.readline

n = int(input())
u = []
for _ in range(n):
    u.append(int(input()))
u.sort()

for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        st, en = j, i
        while st <= en:
            temp = u[st] + u[j] + u[en]
            if temp == u[i]:
                print(temp)
                exit()
            if temp > u[i]:
                en -= 1
            else:
                st += 1