import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

def cal(x, y):
    m = max(abs(x), abs(y))
    s = (m * 2 + 1) ** 2 
    if m == 0:
        return 1
    
    if x == m:
        return (s + (y - m))
    if y == -1 * m:
        return (s - m * 2 + (x - m))
    if x == -1 * m:
        return (s - m * 4 - (y + m))
    if y == m:
        return (s - m * 6 - (x + m))
    
max_len = 0
len = 0
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        max_len = max(max_len, cal(i, j))

while max_len > 0:
    len += 1
    max_len //= 10


for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        print("%*d" %(len, cal(i, j)), end = " ")
    print()
