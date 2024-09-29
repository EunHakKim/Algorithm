import sys
input = sys.stdin.readline

learned = [False] * 26
ans = 0

n, k = map(int, input().split())
words = [set(input().strip()) for _ in range(n)]
for c in ('a', 'c', 'i', 'n', 't'):
    learned[ord(c) - ord('a')] = True

def backtracking(index, depth):
    global ans
    if depth == k - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learned[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        ans = max(ans, readcnt)
        return

    for i in range(index, 26):
        if not learned[i]:
            learned[i] = True
            backtracking(i, depth + 1)
            learned[i] = False

if k < 5:
    print(0)
    exit()
backtracking(0, 0)
print(ans)