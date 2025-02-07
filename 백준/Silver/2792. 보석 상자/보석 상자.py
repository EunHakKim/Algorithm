import sys
input = sys.stdin.readline

n, m = map(int, input().split())
colors = []
for _ in range(m):
    colors.append(int(input()))

st, en = 1, max(colors)
ans = 0

while st <= en:
    mid = (st + en) // 2
    cnt = 0
    for i in range(m):
        cnt+= colors[i]//mid
        if colors[i]%mid!=0:
            cnt+=1
    if cnt>n:
        st=mid+1
    else:
        en=mid-1
        ans=mid
print(ans)