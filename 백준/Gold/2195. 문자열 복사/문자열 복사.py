import sys
input = sys.stdin.readline

s = input().strip()
p = input().strip()
ans = 0
st = 0

while st <= len(p) - 1:
    en = st + 1
    while p[st:en] in s and en < len(p) + 1:
        en += 1
    st = en - 1
    ans += 1

print(ans)