import sys
input = sys.stdin.readline

scores = []
for _ in range(5):
    score = list(map(int, input().split()))
    scores.append(sum(score))
ans = max(scores)
print(scores.index(ans) + 1, ans)