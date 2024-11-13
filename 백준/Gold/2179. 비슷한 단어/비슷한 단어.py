import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

ans_len=0
ans=[]
for i in range(n):
    for j in range(i+1,n):
        word1, word2 = words[i], words[j]
        min_len = min(len(word1), len(word2))
        max_len, length = 0, 0
        for k in range(min_len):
            if word1[k] != word2[k]:
                max_len = max(max_len, length)
                break
            else:
                length += 1
        if length == min_len:
            max_len = max(max_len, length)
        if ans_len < max_len:
            ans = [word1,word2]
            ans_len = max_len

print(ans[0])
print(ans[1])