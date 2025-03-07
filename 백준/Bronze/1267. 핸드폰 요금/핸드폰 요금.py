import sys
input = sys.stdin.readline

n = int(input())
ctime = list(map(int, input().split()))
m, y = 0, 0
for time in ctime:
    y += ((time // 30 + 1) * 10)
    m += ((time // 60 + 1) * 15)

if m == y:
    print("Y M", m)
elif m > y:
    print("Y", y)
else:
    print("M", m)