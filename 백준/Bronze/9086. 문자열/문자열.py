n=int(input())

s=[input() for _ in range(n)]

for i in range(n):
    print(s[i][0]+s[i][-1])