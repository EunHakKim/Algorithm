N = int(input())
M = int(input())
cnt = abs(100 - N)

if M != 0: 
    remote = list(input().split())
else:
    remote = []

for i in range(1000001):
    for j in str(i):
        if j in remote:
            break
    else:
        cnt = min(cnt, len(str(i)) + abs(i - N))

print(cnt)