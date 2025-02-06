import sys
input = sys.stdin.readline

n = int(input())
meetings = []
time_table = 0
ans = 0

for _ in range(n):
    meetings.append(tuple(map(int, input().split())))

meetings.sort(key = lambda x : (x[1], x[0]))

for st, en in meetings:
    if time_table <= st:
        ans += 1
        time_table = en

print(ans)
