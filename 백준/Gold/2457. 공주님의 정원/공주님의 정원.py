import sys
input = sys.stdin.readline

n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]
start = [0, 0]
mid = [3, 1]
ans = 0

flowers.sort()

temp = [0, 0, 0, 0]
for flower in flowers:
    if flower[0] > mid[0] or (flower[0] == mid[0] and flower[1] > mid[1]):
        if temp == [0, 0, 0, 0]:
            print(0)
            exit()
        ans += 1
        start = mid
        mid = [temp[2], temp[3]]
        if temp[2] == 12:
            print(ans)
            exit()
        temp = [0, 0, 0, 0]

    if flower[0] < start[0] or (flower[0] == start[0] and flower[1] < start[1]):
        continue
    
    if flower[2] > temp[2] or (flower[2] == temp[2] and flower[3] > temp[3]):
        if not (flower[0] > mid[0] or (flower[0] == mid[0] and flower[1] > mid[1])):
            temp = flower

    if temp[2] == 12:
            ans += 1
            print(ans)
            exit()

print(0)