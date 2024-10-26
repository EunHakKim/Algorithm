import sys
input = sys.stdin.readline

n = int(input())
words = []
cnt = {}
ans = 0
temp = 9
for _ in range(n):
    arr = list(input().strip())
    arr.reverse()
    words.append(arr)

for word in words:
    for i in range(len(word)):
        if word[i] in cnt:
            cnt[word[i]] += 10 ** i
        else:
            cnt[word[i]] = 10 ** i

sorted_cnt = sorted(cnt.values(), reverse=True)
for value in sorted_cnt:
    ans += value * temp
    temp -= 1

print(ans)